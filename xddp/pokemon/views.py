import json

from django.http import HttpResponse
from .models import Pokemon, Player

from django.core import serializers

###################################################
#TODO:                                            #
#Stop being a lazy fuck and do some proper methods#
###################################################


def Home(request):
    """
    To be deleted
    """
    return HttpResponse("Hi")

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

def importAll(request):
    """
    Import the 151 pokemon from PokeApi into your local database
    """
    #    for i in range(1,152):
    #       Pokemon.ImportOne(i)
    pass
