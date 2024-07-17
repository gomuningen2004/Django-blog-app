from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-postTime', '-postDate']


class ArticleDeatilView(DetailView):
    model = Post
    template_name = 'articleDetail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addPost.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editPost.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')
