from django.shortcuts import render
from .models import Video
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.

class VideoDetail(APIView):
    def get(self, request):
        video = Video.objects.all()
        serializer = VideoSerializer(video, many=True)
        return Response(serializer.data)
    
    def get(self,request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)