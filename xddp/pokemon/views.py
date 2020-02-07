import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon, Player

from django.core import serializers

###################################################
#TODO:                                            #
#Stop being a lazy fuck and do some proper methods#
###################################################


def addPlayer(request):
    Player.create()
    return HttpResponse("Player added")

def getPlayers(request):
    list = Player.objects.all()
    json = serializers.serialize('json', list)

    return HttpResponse(json, content_type="application/json")

def getOwnPokemon(request):
    #TODO:
    #Get several pokes and serialize them into a nice json
    player = Player.objects.get(id=1)
    pokes = Pokemon.objects.get(id_player=player)
    #json = serializers.serialize('json', pokes)

    return HttpResponse(pokes)

def addOneRandom(request):
    """
    :param playerId: Id of the player the Poke should be added
    """
    Pokemon.create()
    return HttpResponse("PokeAdded")

def getAll(request):
    """
    Gets all Pokemon existing in the database
    """
    data = Pokemon.getList()
    json = serializers.serialize('json', data)


    return HttpResponse(json, content_type="application/json")

def home(request):
    context = {'home': 'home'}
    return render(request, "home.html", context)
