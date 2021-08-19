from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    video = models.FileField(upload_to='video',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    website=models.URLField(blank=True)
    caption=models.CharField(max_length=264)
    upload_date=models.DateTimeField(auto_now_add=True)
    update_to=models.DateTimeField(auto_now=True)
    catagory=models.CharField(max_length=100)
    description=models.TextField(null=True)
    class Meta:
        ordering=['-update_to']

class Likes(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='liked_post')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} : {} '.format(self.user , self.post)

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.TextField(verbose_name='Enter comment')
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment


# class PostUrl(models.Model):
#     author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
#     website=models.URLField()
#     caption=models.CharField(max_length=264,blank=True)
#     upload_date=models.DateTimeField(auto_now_add=True)
#     update_to=models.DateTimeField(auto_now=True)
#     catagory=models.CharField(max_length=100,blank=True)
#     description=models.TextField(blank=True)
#     class Meta:
#         ordering=['-upload_date']