from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sai(request):
    return HttpResponse('<b><h1>Django is the one of the framework in python which is used for web development</h1></b>')