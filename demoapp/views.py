from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Home Page")
def demo(request):
    return HttpResponse("Welcome to the Demo Page")
