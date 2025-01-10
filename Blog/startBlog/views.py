from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__' #to get all fields in the Post method if needed separately then we can just use (field names separated by ,)