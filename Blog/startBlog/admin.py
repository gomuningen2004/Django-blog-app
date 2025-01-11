from django.contrib import admin
from .models import Post, Category

admin.site.register(Post) #access posts from the admin area
admin.site.register(Category)