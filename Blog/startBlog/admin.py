from django.contrib import admin
from .models import Post, Category, Profile

admin.site.register(Post) #access posts from the admin area
admin.site.register(Category)
admin.site.register(Profile)