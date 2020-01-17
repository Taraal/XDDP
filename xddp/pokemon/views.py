from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.

def Home(request):
    return HttpResponse("Hi")

def getAll(request):
    data = Pokemon.objects.all()
    return HttpResponse(data)