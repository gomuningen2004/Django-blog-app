from django import forms
from .models import Post, Category

# choices = [('#general', '#general'), ('#Tech', '#Tech'), ('#Career advice', '#Career advice'),] #this is a hardcode way to add the choices

choices  = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            # 'author' : forms.Select(attrs={'class' : 'form-control'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'currentUser', 'value' : '', 'type' : 'hidden'}),
            'category' : forms.Select(choices= choice_list, attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            # 'author' : forms.Select(attrs={'class' : 'form-control'}),
            'category' : forms.Select(choices= choice_list, attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }