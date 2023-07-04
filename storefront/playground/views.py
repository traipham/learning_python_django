from django.shortcuts import render
from django.http import HttpResponse
"""
File: views.py
Description: Request handlers file
request -> response
"""

# Create your views here.

def calculate(x:int = 1, y:int = 2):
    return x * y

def say_hello(request) -> HttpResponse:
    res = calculate()
    dict_val = {'name': 'Trai'}
    return render(request, 'hello.html', dict_val)
    # return HttpResponse('Hello World')