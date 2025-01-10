from django.db import models
from django.contrib.auth.models import User #importing users

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tags = models.CharField(max_length=255, default="Posts.") #as this field is added later to make sure that the old posts dont have any null values we pass some default value that can be stored
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If user is deleted then this removes all the posts from the user
    body = models.TextField()
    

    def __str__(self):
        return self.title + " | " + str(self.author)