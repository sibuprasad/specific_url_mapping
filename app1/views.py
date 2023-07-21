from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse ("<h1>My first function</h1>")

def second(request):
    return HttpResponse("<h1>My second function</h1>")