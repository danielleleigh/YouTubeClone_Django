from django.db.models import fields
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['video_id', 'title', 'description', 'comment', 'like', 'dislike']