from django.db import models
import requests
# Create your models here.


#######################
# PLAYER AND SECURITY #
#######################

class Object(models.Model):
    """
    :param label
    """
    label = models.TextField()


class Player(models.Model):
    """
    :param username
    :param HASH password
    :param email
    :param name
    :param surname
    :param dob (DateOfBirth)
    :param MTMObject objects_list
    """
    username = models.TextField(null=True)
    password = models.TextField(null=True)
    email = models.TextField(null=True)
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    dob = models.TextField(null=True)
    objects_list = models.ManyToManyField(Object, through='Inventory')

    def __str__(self):
        return self.username

    # TODO :
    # Add a proper create method for Player
    @classmethod
    def create(cls):
        player = cls(name="Sylouan")
        player.save()
        return player

    def create(cls, username=None, password=None, email=None, surname=None, dob=None, objects_list=None):
        player = Player(cls, username=username, password=password,
                        email=email, surname=surname, dob=dob, objects_list=objects_list)
        player.save()

    @classmethod
    def getAll(cls):
        """
        Gets all the players in the database
        :rtype: Player Queryset
        """

        fullList = Player.objects.all()

        return fullList

    def getPlayer(cls, username):
        try:
            player = Player.objects.get(username=username)

            return player
        except Exception as e:
            return "Player not found"


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

    @classmethod
    def getAllFromPlayer(cls, id_player=None):
        """

        :param id_player: id of the player searched for
        :type id_player: int
        :return: A list of all the teams the player has
        :rtype: PokemonTeam Queryset
        """
        try:
            player = Player.objects.get(id=id_player)
        except Exception as e:
            return "Player not found"

        list = PokemonTeam.objects.filter(id_player=player)

        return list

    @classmethod
    def create(cls, player_id=None, name=None):
        try:
            player = Player.objects.get(id=player_id)
        except Exception as e:
            return "Player not found"

        new_team = cls(id_player=player, name=name)
        new_team.save()

        return new_team


class Type(models.Model):
    """
    :param id_type
    :param nom
    :param FKEYType double_damage_from(null)
    :param FKEYType double_damage_to(null)
    :param FKEYType half_damage_from(null)
    :param FKEYType half_damage_to(null)
    :param FKEYType no_damage_from(null)
    :param FKEYType no_damage_to(null)
    """
    id_type = models.IntegerField(null=True)
    name = models.CharField(max_length=50, null=True)
    double_damage_from = models.ManyToManyField("self")
    double_damage_to = models.ManyToManyField("self")
    half_damage_from = models.ManyToManyField("self")
    half_damage_to = models.ManyToManyField("self")
    no_damage_from = models.ManyToManyField("self")
    no_damage_to = models.ManyToManyField("self")

class Move(models.Model):
    """
    :param id_move
    :param name(null)
    :param power(null)
    :param FKEYType types
    """
    name = models.CharField(max_length=50, null=True)
    power = models.IntegerField(null=True)
    types = models.ManyToManyField(Type)

    @classmethod
    def ImportOne(cls, id):
        """
        Allows one to import a specific move from pokeapi
        :param id:
        """

        if not Move.objects.filter(id_attack=id).exists():
            url = "https://pokeapi.co/api/v2/move/"

            data = requests.get(url + str(id)).json()
            name = data['name']
            power = data['power']
            types = data['type'][1]

            move = cls(name=name, power=power, types=types)
            move.save()
        else:
            move = Move.objects.get(id_attack=id)
        return move


class Pokemon(models.Model):
    """
    :param speed
    :param atk
    :param defense
    :param hp
    :param current_hp
    :param name
    :param FKEYType types
    :param FKEYPoke id_poke(null)
    :param FKEYPlayer id_player
    :param FKEYTeam id_team
    """
    speed = models.IntegerField(null=True)
    atk = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    current_hp = models.IntegerField(null=True)
    name = models.CharField(max_length=50, null=True)
    level = models.IntegerField(null=True)
    exp = models.IntegerField(null=True)
    types = models.ManyToManyField(Type)
    id_poke = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    id_player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    id_team = models.ForeignKey(
        PokemonTeam, on_delete=models.CASCADE, null=True)
    moves = models.ManyToManyField(Move)

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

    @classmethod
    def getFromTeam(cls, id_team=None):
        """

        :param id_team: id of the searched team
        :type id_team: int
        :return: All pokemons from a specific team
        :rtype: Pokemon Queryset
        """

        try:
            team = PokemonTeam.objects.get(id=id_team)
        except Exception as e:
            return "Team not found"

        list = Pokemon.objects.filter(id_team=team)

        return list

    # TODO:
    # Add a proper create method for Pokemon
    @classmethod
    def create(cls):
        player = Player.objects.get(id=1)
        pokeOne = Pokemon.objects.get(id=1)
        newpoke = cls(name="Pokemon", id_player=player, id_poke=pokeOne)
        newpoke.save()
        return newpoke

    @classmethod
    def create(cls, player_id=None, pokemon_id=None, team_id=None, atk=None, hp=None, defense=None,
               name=None, level=None, exp=None, speed=None,):
        try:
            player = Player.objects.get(id=player_id)
        except Exception as e:
            return "Player not found"

        try:
            team = PokemonTeam.objects.get(id=team_id)
        except Exception as e:
            return "Team not found"

        new_poke = cls(name=name, level=level, exp=exp, speed=speed, atk=atk, defense=defense,
                       team_id=team, pokemon_id=pokemon_id, player_id=player)
        new_poke.save()

        return new_poke

    @classmethod
    def getList(cls, id_max=152):
        """
        :param id_max : Max id returned from database (default: 152)
        """
        pokeList = Pokemon.objects.all().filter(id__lte=id_max)
        return pokeList


#########
# ZONES #
#########

class Zone(models.Model):

    name = models.TextField(null=True)
    min_level = models.IntegerField(null=True)
    max_level = models.IntegerField(null=True)
    allowed_pokemon = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, allowed_pokemon, min_level=2, max_level=12):
        new_zone = cls(name=name, allowed_pokemon=allowed_pokemon,
                       min_level=min_level, max_level=max_level)

        new_zone.save()


class Inventory(models.Model):
    """
    :param FKEYPlayer player
    :param FKEYObject item
    :param quantity
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    item = models.ForeignKey(Object, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @classmethod
    def getInventory(cls, idPlayer):
        bagOfHolding = Inventory.objects.filter(player=idPlayer)
        return bagOfHolding
