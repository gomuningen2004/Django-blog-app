from django.urls import path
# from . import views
from .views import HomeView, ArticleDeatilView, AddPostView

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDeatilView.as_view(), name="articleDetail"),
    path('addNewPost/', AddPostView.as_view(), name='addPost'),
]
