from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse(" Welcome to Mundesign Jewelers ")

def demo(request):
    return HttpResponse("Please follow the Website")

