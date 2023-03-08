from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app5_first(request):
    return HttpResponse('<h1>This is the first function in app5</h1>')

def app5_second(request):
    return HttpResponse('<h1><marquee>This is the second function in app5<marquee></h1>')
