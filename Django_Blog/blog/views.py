import json
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, NameCount
from rest_framework import viewsets
from .serializers import PostSerializer, NameCountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    posts = Post.objects.filter(isConfirmed=True)
    return render(request, 'blog/post_list.html', {'posts' : posts})

def confirm_post_list(request):
    posts = Post.objects.filter(isConfirmed=False)
    return render(request, 'blog/confirm_post_list.html', {'posts' : posts})

from django.conf import settings

def api_confirm_post_list(request):
    posts = Post.objects.filter(isConfirmed=False)
    posts_data = []

    for post in posts:
        post_dict = {
            "title": post.title,
            "text": post.text,
            # 기타 필요한 필드 ...
            "image_url": request.build_absolute_uri(settings.MEDIA_URL + str(post.image)),
            "pk" : post.pk
        }
        posts_data.append(post_dict)

    return JsonResponse(posts_data, safe=False)

def post_save(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.isConfirmed = True
    post.text = "This is Confirmed at  " + str(timezone.now())
    post.save()

    try:
        name_count = NameCount.objects.get(name=post.title)
        name_count.count += 1
    except NameCount.DoesNotExist:
        # If the name does not exist, create a new record with count=1
        name_count = NameCount(name=post.title, count=1)
    
    name_count.save()

    return redirect('/confirm')

def post_discard(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/confirm')

def main_page(request):
    name_counts = NameCount.objects.all()
    data = serializers.serialize('json', name_counts)

    return render(request, 'main_page.html', {'name_counts': data})

class IncrementNameCountView(viewsets.ModelViewSet):
    queryset = NameCount.objects.all()
    serializer_class = NameCountSerializer

    def create(self, request):
        name = request.data.get('name')
        if name:
            # Try to find a NameCount with the given name
            try:
                name_count = NameCount.objects.get(name=name)
                name_count.count += 1
            except NameCount.DoesNotExist:
                # If the name does not exist, create a new record with count=1
                name_count = NameCount(name=name, count=1)
            
            name_count.save()
            return Response({'message': f'Count for {name} incremented successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Name not provided in the request.'}, status=status.HTTP_400_BAD_REQUEST)

