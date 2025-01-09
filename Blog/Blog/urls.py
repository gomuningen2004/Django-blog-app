from django.contrib import admin
from django.urls import path, include #include is added so that we can import from the apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('startBlog.urls')), #adding the app urls here
]
