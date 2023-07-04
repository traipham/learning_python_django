from django.urls import path
from . import views
"""
Name:
Description: Map URLS to view requests
"""
# url configuration
urlpatterns = [
    path('hello/', views.say_hello)
]