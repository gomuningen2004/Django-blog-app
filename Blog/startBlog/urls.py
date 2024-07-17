from django.urls import path
# from . import views
from .views import HomeView, ArticleDeatilView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDeatilView.as_view(), name="articleDetail"),
    path('addNewPost/', AddPostView.as_view(), name='addPost'),
    path('editPost/<int:pk>', EditPostView.as_view(), name='editPost'),
    path('deletePost/<int:pk>', DeletePostView.as_view(), name='deletePost'),
]
