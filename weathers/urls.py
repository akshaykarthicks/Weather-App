"""
URL configuration for weathers project.
"""
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weathers.Weather.urls')),
]
