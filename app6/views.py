from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def app6_first(request):
    return HttpResponse('<h1>this is the first function in app6<h1>')


def app6_second(request):
    return HttpResponse('<h1><marquee>this is the second function in app6<marquee><h1>')



