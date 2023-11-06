from blog.models import Post, NameCount
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'created_date', 'published_date', 'image')
        # fields = '__all__'

class NameCountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NameCount
        fields = ('name',)
        # fields = '__all__'