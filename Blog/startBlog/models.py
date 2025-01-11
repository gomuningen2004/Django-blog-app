from django.db import models
from django.contrib.auth.models import User #importing users
from django.urls import reverse #importing the reverse function for the posting button
from datetime import datetime, date, time

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    # title_tags = models.CharField(max_length=255, default="Posts.") #as this field is added later to make sure that the old posts dont have any null values we pass some default value that can be stored
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If user is deleted then this removes all the posts from the user
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default="#general") #make sure that the categories doesn't contain special characters and the letters are always small letters not capital letters

    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')
