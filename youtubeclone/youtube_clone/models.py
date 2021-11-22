from django.db import models

# Create your models here.

class Video(models.Model):
    video_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    like = models.CharField(max_length=50)
    dislike = models.CharField(max_length=50)