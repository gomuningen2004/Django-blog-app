from django.urls import path
# from . import views #importing views.py file from thecurrent dir
from .views import HomeView
urlpatterns = [
    # path('', views.home, name="home"), #'' is blank so that the url doesnt have /home or anything like that, and views.home is calling for the home function from the view.py file
    path('', HomeView.as_view(), name="home"),
]
