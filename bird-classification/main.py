import tensorflow as tf
import numpy as np
import pandas as pd
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from glob import glob
from keras.preprocessing import image
from tensorflow.keras import layers
from flask import Flask, request, jsonify


app = Flask(__name__)

IMAGE_RES = 224                                                                 # input dimensions required by the CNN model
def preprocess_image_to_tensor(img_path):
    img = image.load_img(img_path, target_size=(IMAGE_RES, IMAGE_RES))          # loads RGB image as PIL.Image.Image type, resize image to model input dimensions
    x = image.img_to_array(img)/255.0                                           # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3) and normalize to [0:1] as per model requierements
    x = np.expand_dims(x, axis=0)                                               # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return x


URL = 'https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1'               # Import pre-trained bird classification model from Tensorflow Hub
bird = hub.KerasLayer(URL, input_shape=(IMAGE_RES,IMAGE_RES,3))                 # Using aiy/vision/classifier/birds_V1 classifying 964 bird species from images. It is based on MobileNet, and trained on photos contributed by the iNaturalist community
bird.trainable=False

model=tf.keras.Sequential([bird])

labels = pd.read_csv("./aiy_birds_V1_labelmap.csv", sep=',', header=0, index_col=0)  # using scientific names  in Latin

label='name'

@app.route('/', methods=["GET"])
def hello_world():
    return "hello"

@app.route('/predict', methods=["POST"])
def predict():
    print("predict!")
    file = request.files['image']
    file.save("./images/" + file.filename)

    my_files = np.array(glob("./images/" + file.filename))
    predictions = []
    for index, file in enumerate(my_files):
        processed_image=preprocess_image_to_tensor(file)
        output = model.predict(processed_image)
        top_5_indices = np.argsort(output, axis=None)[::-1][:5]
        top_5_values = output.ravel()[top_5_indices]

        for i in range(5):
            predicted_label = labels[label][top_5_indices[i]]
            confidence = float(top_5_values[i])  
            predictions.append([predicted_label, confidence])

        prediction = np.argmax(tf.squeeze(output).numpy())
        last_prediction = labels[label][prediction]

    data = {"predictions" : predictions, "answer" : last_prediction}

    return jsonify(data)

if __name__ == '__main__':
    print("server init...")
    app.run(host='localhost', port=5000)
