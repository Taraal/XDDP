import json
import os
import requests
from django.http import HttpResponse
from .models import Pokemon, Player

from django.core import serializers

from authenticate.views import hashPass

#########
# SETUP #
#########

def importAll(request):

    ###########
    # SPRITES #
    ###########

    urlback = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/"
    urlfront = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"

    for i in range(1, 152):

        if not os.path.exists('resources/sprites/back/' + str(i) + '.png'):
            rback = requests.get(urlback + str(i) + ".png")
            with open('resources/sprites/back/' + str(i) + '.png', 'wb') as back:
                back.write(rback.content)

        if not os.path.exists('resources/sprites/front/' + str(i) + '.png'):
            with open('resources/sprites/front/' + str(i) + '.png', 'wb') as front:
                rfront = requests.get(urlfront + str(i) + ".png")
                front.write(rfront.content)

        #########
        # ZONES #
        #########


        #########
        # TYPES #
        #########

        ############
        # POKEMONS #
        ############

    for i in range(1, 152):
        Pokemon.ImportOne(i)


##########
# PLAYER #
##########

def addPlayer(request):
    try:
        prenom = request.POST.get("prenom", "")
        nom = request.POST.get("nom", "")
        email = request.POST.get('email', "")
        username = request.POST.get("username", "")
        password = hashPass(request.POST.get("password"))
        user_instance = Player.create(prenom, nom, username, email, password)
        user_instance.save()
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(True)



def getPlayers(request):
    list = Player.objects.all()
    json = serializers.serialize('json', list)

    return HttpResponse(json, content_type="application/json")

def getOnePlayer(request, idPlayer):
    try:
        player = Player.objects.filter(pk=idPlayer)
        json = serializers.serialize('json', player)
    except Exception as e:

        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')

###########
# POKEMON #
###########

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


def getOnePokemon(request, idPoke):
    try:
        poke = Pokemon.objects.filter(pk=idPoke)

        json = serializers.serialize('json', poke)

    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')