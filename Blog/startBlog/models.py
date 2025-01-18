from django.db import models
from django.contrib.auth.models import User #importing users
from django.urls import reverse #importing the reverse function for the posting button
from datetime import datetime, date, time
from ckeditor.fields import RichTextField

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
    # body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=255) #make sure that the categories doesn't contain special characters and the letters are always small letters not capital letters
    likes = models.ManyToManyField(User, related_name="blog_likes")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('post-detail', args=(str(self.id)))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)