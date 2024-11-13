# myproject2/urls.py
from django.contrib import admin
from django.urls import path, include  # Include function is used to include other URLconfs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', include('blog.urls')),   # Include URLs from the 'blog' app
]
