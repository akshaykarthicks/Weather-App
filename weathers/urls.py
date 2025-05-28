"""
URL configuration for weathers project.
"""
from django.urls import path, include

urlpatterns = [
    path('', include('weathers.weathers.urls')),
]
