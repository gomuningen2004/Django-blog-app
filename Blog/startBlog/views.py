from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {}) #making a new view called home that calles for home.html file and {} is to give any parameters

#ListView returns all the posts
#DetailView return the whole detail of one single post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id'] #-id is sorting from last to first and just id is sorting from first to last
    ordering = ['-post_date', '-post_time']

class PostView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' #to get all fields in the Post method if needed separately then we can just use (field names separated by ,)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'body'] #when having form_class we cant have fields

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')