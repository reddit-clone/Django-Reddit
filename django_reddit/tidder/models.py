from django.db import models
from datetime import datetime
# Create your models here.
class Post (models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length= 255)
    picture = models.CharField(max_length=400, blank = True)
    content = models.TextField()
    site_url = models.CharField(max_length=400)
    vote_total = models.CharField(max_length=255)

    def __str__ (self):
        return self.title

class Comment(models.Model):
     created_at = models.DateTimeField(default=datetime.now, blank=True)
     content = models.TextField()  
     vote_total = models.CharField(max_length=255)  
     post = models.ForeignKey(Post, on_delete= models.CASCADE, blank=True, related_name='posts')

     def __str__ (self):
         return self.content

class User(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=16)

    def __str__ (self):
        return self.username

class Profile(models.Model):
    profile_pic = models.CharField(max_length=255)
    user = models.ForeignKey(Post, on_delete = models.CASCADE, blank=True, related_name='users')

    def __str__ (self):
        return self.user













