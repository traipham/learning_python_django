from django.shortcuts import render
from django.http import HttpResponse
"""
File: views.py
Description: Request handlers file
request -> response
"""

# Create your views here.

def say_hello(request) -> HttpResponse:
    return HttpResponse('Hello World')
