from django.urls import path
# from . import views #importing views.py file from thecurrent dir
from .views import HomeView, PostView, AddPostView, UpdatePostView
urlpatterns = [
    # path('', views.home, name="home"), #'' is blank so that the url doesnt have /home or anything like that, and views.home is calling for the home function from the view.py file
    path('', HomeView.as_view(), name="home"), #using the class views
    path('post/<int:pk>', PostView.as_view(), name="post-detail"), #the <int:pk> is passing the primary key as a parameter
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('edit_post/<int:pk>', UpdatePostView.as_view(), name="edit-post"),
]
