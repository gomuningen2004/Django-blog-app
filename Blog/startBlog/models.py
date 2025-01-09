from django.db import models
from django.contrib.auth.models import User #importing users

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If user is deleted then this removes all the posts from the user
    body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.author)