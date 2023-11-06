from django.shortcuts import render
from .models import Post, NameCount
from rest_framework import viewsets
from .serializers import PostSerializer, NameCountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.http import JsonResponse

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})

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

