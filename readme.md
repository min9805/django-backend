:video_camera: [DEMO VIDEO](https://youtu.be/ETcNTVAwpQE) | :computer: [MODEL TRAINING & EVALUATION DETAILS](https://tfhub.dev/google/aiy/vision/classifier/birds_V1/1)

# Bird Species Classification by Yolov5

This repository contains Django Server, Bird Classifier, Yolov5

![image](https://github.com/min9805/django-backend/assets/56664567/3e899754-ef27-4149-9971-bfadad0b6bcd)

## Objective

 Changes are detected through Yolov5. At this time, if the changed object is a bird, what type it is is determined through a classifier. Django shows a graph showing how many types of birds have appeared, and when a pre-designated specific type of bird appears, it posts the corresponding photo and the results of the classifier.

## Getting Started

1. Connect to each venv and run `pip install -r requrements.txt`.
2. Classifier : `python main.py`
3. Django : `python manage.py runserver`
4. Yolov5 : `python detect.py --source 0`

