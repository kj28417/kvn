from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("hello Django")

def by(request):
    return HttpResponse("Creado por Kevin Lopez")