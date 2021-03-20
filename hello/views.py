from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hi. Welcome to CJ's book inventory")
