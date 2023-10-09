from django.shortcuts import render
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})