from django.db import models
import requests
# Create your models here.


#######################
# PLAYER AND SECURITY #
#######################

class Player(models.Model):
    """
    :param username
    :param HASH password
    :param email
    :param name
    :param surname
    :param dob (DateOfBirth)
    """
    username = models.TextField(null=True)
    password = models.TextField(null=True)
    email = models.TextField(null=True)
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    dob = models.TextField(null=True)

    def __str__(self):
        return self.username

    # TODO :
    # Add a proper create method for Player
    @classmethod
    def create(cls):
        player = cls(name="Sylouan")
        player.save()
        return player


#############################
# POKEMON AND POKEMON TEAMS #
#############################


class PokemonTeam(models.Model):
    """

    :param id_player
    :param name
    """
    id_player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    """
    :param speed
    :param atk
    :param defense
    :param hp
    :param name
    :param FKEYPoke id_poke(null)
    :param FKEYPlayer id_player
    :param FKEYTeam id_team
    """
    speed = models.IntegerField(null=True)
    atk = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)
    level = models.IntegerField(null=True)
    exp = models.IntegerField(null=True)
    id_poke = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    id_player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    id_team = models.ForeignKey(PokemonTeam, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + str(self.id)

    @classmethod
    def ImportOne(cls, id):
        """
        Allows one to import a specific base Pokemon from pokeapi
        :param id:
        """

        if not Pokemon.objects.filter(id_poke=id).exists():
            url = "https://pokeapi.co/api/v2/pokemon/"

            data = requests.get(url + str(id)).json()
            name = data['name']

            speed = data['stats'][0]['base_stat']
            atk = data['stats'][4]['base_stat']
            defense = data['stats'][3]['base_stat']
            hp = data['stats'][5]['base_stat']

            poke = cls(atk=atk, defense=defense, speed=speed, hp=hp, name=name)
            poke.save()
        else:
            poke = Pokemon.objects.get(id_poke=id)
        return poke


    #TODO:
    #Add a proper create method for Pokemon
    @classmethod
    def create(cls):
        player = Player.objects.get(id=1)
        pokeOne = Pokemon.objects.get(id=1)
        newpoke = cls(name="Pokemon", id_player=player, id_poke=pokeOne)
        newpoke.save()
        return newpoke


    @classmethod
    def getList(cls, id_max=152):
        """
        :param id_max : Max id returned from database (default: 152)
        """
        pokeList = Pokemon.objects.all().filter(id__lte=id_max)
        return pokeList
