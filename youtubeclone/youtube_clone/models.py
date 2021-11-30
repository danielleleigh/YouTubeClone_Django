from django.db import models

# Create your models here.

class Comment(models.Model):
    video_id = models.CharField(max_length=50) 
    comment = models.CharField(max_length=50)
    like = models.IntegerField(max_length=50, null=0)
    dislike = models.IntegerField(max_length=50, null=0)
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    reply = models.CharField(max_length=50)
    
 