from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse ("<h1>First function for app2</h1>")

def second(request):
    return HttpResponse ("<h1>Second function for app2</h1>")