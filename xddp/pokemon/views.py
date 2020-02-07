import json
import random
from django.http import HttpResponse
from .models import Pokemon, Player

from django.core import serializers

from authenticate.views import hashPass

###################################################
#TODO:                                            #
#Stop being a lazy fuck and do some proper methods#
###################################################


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
    # TODO:
    # Get several pokes and serialize them into a nice json
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

###########
# BATTLE  #
###########


def rollCritRate(idAttack):
    try:
        # Si l'attaque est une attaque differente d'une attaque physique ou speciale (donc pas de statuts)
        # Lance un roll (1 chance sur 24)
        # Si ça tombe sur 12, renvoi true, sinon false
        critOrNot = False
        valueRoll = randrange(1, 24)
        if valueRoll == 12:
            critOrNot = True
    except Exception as e:
        return ValueError(e)
    return critOrNot


def calculMultiplierCoefficient(idPokemonAttaquant, idPokemonDefenseur, idAttack):
    # Coefficients Multiplicateurs
    # le STAB => 1 ou 1,5
    # l'efficacité du type de la capacité; => 0 ou 0,5 ou 1 ou 2 ou 4
    # un nombre généré aléatoirement compris entre 0.85 et 1.
    try:
        CM = 1
        pokemonAttaquant = Pokemon.objects.filter(pk=idPokemonAttaquant)
        pokemonDefenseur = Pokemon.objects.filter(pk=idPokemonDefenseur)
        Move = Move.objects.filter(pk=idAttack)

        # STAB
        for items in pokemonAttaquant.types:
            if pokemonAttaquant.types[items] == Move.types:
                CM = CM + 0.5

        # Efficacité
        efficiencyTypesValue = 1

        if pokemonDefenseur.types.double_damage_from.filter(name=Move.types).exists():
            efficiencyTypesValue = efficiencyTypesValue * 2
        if pokemonDefenseur.types.half_damage_from.filter(name=Move.types).exists():
            efficiencyTypesValue = efficiencyTypesValue / 2
        if pokemonDefenseur.types.no_damage_from.filter(name=Move.types).exists():
            efficiencyTypesValue = efficiencyTypesValue * 0

            # Random roll
        roll = random.randrange(0.85, 1)
        CM = CM * roll

        CM = CM * efficiencyTypesValue

    except Exception as e:
        return ValueError(e)

    return CM


def doFight(request, idPokemonAttaquant, idPokemonDefenseur, idAttack):
    try:
        pokemonAttaquant = Pokemon.objects.filter(pk=idPokemonAttaquant)
        pokemonDefenseur = Pokemon.objects.filter(pk=idPokemonDefenseur)
        move = Move.objects.filter(pk=idAttack)

        dmgDone = ((((pokemonAttaquant.Level*0.4+2) *
                     pokemonAttaquant.Atk * move.power)/(pokemonDefenseur.Def * 50))+2) * calculMultiplierCoefficient(idPokemonAttaquant, idPokemonDefenseur, idAttack)

        json = serializers.serialize('json', dmgDone)

    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')
