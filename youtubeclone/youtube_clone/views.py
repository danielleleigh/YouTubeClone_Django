from django.shortcuts import render
from .serializers import CommentSerializer, ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Comment, Reply

# Create your views here.

class CommentList(APIView):
    def get(self, request):
        video = Comment.objects.all()
        serializer = CommentSerializer(video, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    #get by id
    def get(self, request, pk):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(Comment)
        return Response(serializer.data)

    #update
    def put(self, request, pk):
        Comment = self.get_object(pk)
        serializer = CommentSerializer(Comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReplyList(APIView):
    def get(self, request):
        video = Reply.objects.all()
        serializer = ReplySerializer(video, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReplyDetail(APIView):

    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404

    #get by id
    def get(self, request, pk):
        Reply = self.get_object(pk)
        serializer = ReplySerializer(Reply)
        return Response(serializer.data)

    #update
    def put(self, request, pk):
        Reply = self.get_object(pk)
        serializer = ReplySerializer(Reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk):
        reply = self.get_object(pk)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)