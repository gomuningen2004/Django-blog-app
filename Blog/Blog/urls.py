from django.contrib import admin
from django.urls import path, include #include is added so that we can import from the apps
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('startBlog.urls')), #adding the app urls here
    path('members/', include('django.contrib.auth.urls')), #handles the user auth side like login and registration
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
