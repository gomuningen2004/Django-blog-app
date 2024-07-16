from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDeatilView(DetailView):
    model = Post
    template_name = 'articleDetail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'