import os
import requests
import random

import random
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from authenticate.views import hashPass
from .models import Pokemon, Player, Zone, Move, Inventory,     Object, Type


##########
# PLAYER #
##########

@csrf_exempt
def addPlayer(request):
    try:
        prenom = request.POST.get("prenom", "")
        nom = request.POST.get("nom", "")
        email = request.POST.get('email', "")
        username = request.POST.get("username", "")
        password = hashPass(request.POST.get("password"))
        user_instance = Player(name=prenom, surname=nom, username=username, email=email, password=password)
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


def getOwnPokemon(request, idPlayer):
    """
    Returns all pokemons of the player
    :param idPlayer: id of the wanted player
    :type idPlayer: int
    :return: All the player's pokemon
    :rtype: json
    """
    try:
        player = Player.objects.get(id=idPlayer)
        pokes = Pokemon.objects.filter(id_player=player)
        #json = serializers.serialize('json', pokes)
    except Exception as e :
        return HttpResponse(e)

    return HttpResponse(pokes)


def addOneRandom(request, idPlayer):
    """
    :param idPlayer: Id of the player the Poke should be added
    """
    try:
        player = Player.objects.get(pk=idPlayer)

        original_poke = Pokemon.objects.get(pk=random.randrange(1, 151))

        new_poke = Pokemon(speed=original_poke.speed,
                           id_player=player,
                           id_poke=original_poke
                           )

        new_poke.save()

    except Exception as e:
        return HttpResponse(e)
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

     # Creation de tous les types, puis les save
    rangeNumberTypes = 0
    url = "https://pokeapi.co/api/v2/type/"
    data = requests.get(url).json()
    rangeNumberTypes = data['count'] - 2
    for a in range(0, rangeNumberTypes):
        name = data['results'][a]['name']
        type = Type(name=name)
        type.save()
    # Creation de tous les types, puis les save
    # type crée.doubledmgfrom.add(type.object.get(name=nameoftype))

    for t in range(1, rangeNumberTypes):
        url = "https://pokeapi.co/api/v2/type/"

        data = requests.get(url + str(t)).json()
        name = data['name']

        for index, item in enumerate(data['damage_relations']['double_damage_from']):
            type.double_damage_from.add(Type.objects.get(
                name=data['damage_relations']['double_damage_from'][index]['name']))
        for index,item in enumerate(data['damage_relations']['double_damage_to']):
            type.double_damage_to.add(Type.objects.get(
                name=data['damage_relations']['double_damage_to'][index]['name']))
        for index,item in enumerate(data['damage_relations']['half_damage_from']):
            type.half_damage_from.add(Type.objects.get(
                name=data['damage_relations']['half_damage_from'][index]['name']))
        for index, item in enumerate(data['damage_relations']['half_damage_to']):
            type.half_damage_to.add(Type.objects.get(
                name=data['damage_relations']['half_damage_to'][index]['name']))
        for index, item in enumerate(data['damage_relations']['no_damage_from']):
            type.no_damage_from.add(Type.objects.get(
                name=data['damage_relations']['no_damage_from'][index]['name']))
        for index, item in enumerate(data['damage_relations']['no_damage_to']):
            type.no_damage_to.add(Type.objects.get(
                name=data['damage_relations']['no_damage_to'][index]['name']))

        type.save()


    return HttpResponse(json, content_type='application/json')



def purgeAll(request):

    Zone.objects.all().delete()
    Pokemon.objects.all().delete()
    Type.objects.all().delete()

    os.system("../manage.py sqlsequencereset pokemon")

    return HttpResponse('BDD purgée')


def rollCritRate(idAttack):
    try:
        # Si l'attaque est une attaque differente d'une attaque physique ou speciale (donc pas de statuts)
        # Lance un roll (1 chance sur 24)
        # Si ça tombe sur 12, renvoi true, sinon false
        critOrNot = False
        valueRoll = random.randrange(1, 24)
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
        move = Move.objects.filter(pk=idAttack)

        # STAB
        for items in pokemonAttaquant.types:
            if pokemonAttaquant.types[items] == move.types:
                CM = CM + 0.5

        # Efficacité
        efficiencyTypesValue = 1

        if pokemonDefenseur.types.double_damage_from.filter(name=move.types).exists():
            efficiencyTypesValue = efficiencyTypesValue * 2
        if pokemonDefenseur.types.half_damage_from.filter(name=move.types).exists():
            efficiencyTypesValue = efficiencyTypesValue / 2
        if pokemonDefenseur.types.no_damage_from.filter(name=move.types).exists():
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
        dmgDone = 0

        dmgDone = ((((pokemonAttaquant.Level*0.4+2) *
                     pokemonAttaquant.Atk * move.power)/(pokemonDefenseur.Def * 50))+2) * calculMultiplierCoefficient(idPokemonAttaquant, idPokemonDefenseur, idAttack)

        pokemonDefenseur.current_hp = pokemonDefenseur.current_hp - dmgDone

        if pokemonDefenseur.current_hp <= 0:
            pokemonDefenseur.current_hp = 0

        pokemonDefenseur.save()

        json = serializers.serialize('json', pokemonDefenseur)

    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')


##############
# INVENTORY  #
##############


def getPlayerInventory(request, idPlayer):
    try:
        playerInventory = Inventory.objects.filter(player=idPlayer)
        json = serializers.serialize('json', playerInventory)
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')


def addItem(request, idPlayer, idItem, nbrAdd = 1):
    try:
        playerInventory = Inventory.objects.filter(
            player=idPlayer, item=idItem)
        playerInventory.quantity = playerInventory.quantity + nbrAdd
        playerInventory.save()
        json = serializers.serialize('json', playerInventory)
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')


def addItems(request, idPlayer, idItem, nbrAdd):
    try:
        playerInventory = Inventory.objects.filter(
            player=idPlayer, item=idItem)
        playerInventory.quantity = playerInventory.quantity + nbrAdd
        playerInventory.save()
        json = serializers.serialize('json', playerInventory)
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(json, content_type='application/json')
