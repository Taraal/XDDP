from django.shortcuts import render
from django.http import HttpResponse
from pokemon.models import Player

# Create your views here.

def Home(request):
    return HttpResponse("Hi")

def register(request):

    player = Player()
    player.save()


    return HttpResponse("Player registered")