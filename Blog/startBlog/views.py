from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {}) #making a new view called home that calles for home.html file and {} is to give any parameters

#ListView returns all the posts
#DetailView return the whole detail of one single post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostView(DetailView):
    model = Post
    template_name = 'post_detail.html'