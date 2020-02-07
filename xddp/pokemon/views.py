import os
import requests
import random

from django.http import HttpResponse
from django.core import serializers

from authenticate.views import hashPass
from .models import Pokemon, Player, Zone

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
    """
    Gets a single pokemon from the database
    :param idPoke: Id of the wanted pokemon
    :type idPoke: int
    :return: The pokemon and its stats
    :rtype: json
    """
    try:
        poke = Pokemon.objects.filter(pk=idPoke)

        json = serializers.serialize('json', poke)

    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')

def encounter(request, idZone):
    """
    Returns an allowed pokemon in the specified zone
    :param idZone: Id  of the current area
    :type idZone: int
    :return: Random pokemon within the allowed range
    :rtype: pokemon/json
    """
    try:

        zone = Zone.objects.get(pk=idZone)
        random_poke = random.choice(list(zone.allowed_pokemon))
        json = serializers.serialize('json', random_poke)

    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')
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

        if not os.path.exists('pokemon/ resources/sprites/back/' + str(i) + '.png'):
            rback = requests.get(urlback + str(i) + ".png")
            with open('pokemon/resources/sprites/back/' + str(i) + '.png', 'wb') as back:
                back.write(rback.content)

        if not os.path.exists('pokemon/resources/sprites/front/' + str(i) + '.png'):
            with open('pokemon/resources/sprites/front/' + str(i) + '.png', 'wb') as front:
                rfront = requests.get(urlfront + str(i) + ".png")
                front.write(rfront.content)

    ############
    # POKEMONS #
    ############

    for i in range(1, 152):
        Pokemon.ImportOne(i)

    #########
    # ZONES #
    #########

    names = ['Forêt', 'Montagne', 'Mer', 'Volcan']

    allowed_pokes = [
        [1, 2, 3, 10, 11, 16, 20, 23],
        [25, 27, 39, 46, 50, 56, 74, 95],
        [7, 8, 9, 116, 98, 129, 86],
        [4, 5, 6, 37, 58, 77, 126, 136]
    ]

    for i in range(0, 4):

        if not Zone.objects.filter(pk=i+1).exists():

            new_zone = Zone(name=names[i])
            new_zone.save()
            for poke in allowed_pokes[i]:
                new_zone.allowed_pokemon.add(Pokemon.objects.get(pk=poke))

            new_zone.save()

    qset = Zone.objects.all()

    json = serializers.serialize('json', qset)
    #########
    # TYPES #
    #########


    return HttpResponse(json, content_type='application/json')



def purgeAll(request):

    Zone.objects.all().delete()
    Pokemon.objects.all()

    os.system("../manage.py sqlsequencereset pokemon")

    return HttpResponse('BDD purgée')
