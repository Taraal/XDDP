from django.db import models
import requests
# Create your models here.

class Pokemon(models.Model):
    speed = models.IntegerField(null=True)
    atk = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)
    id_poke = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    @classmethod
    def createOne(cls, id):
        if not Pokemon.objects.filter(id_poke=id).exists():
            url = "https://pokeapi.co/api/v2/pokemon/"

            poke = Pokemon.create()
            data = requests.get(url + str(id)).json()
            poke.id = id
            name = data['name']

            speed = data['stats'][0]['base_stat']
            atk = data['stats'][4]['base_stat']
            defense = data['stats'][3]['base_stat']
            hp = data['stats'][5]['base_stat']

            poke = cls(id_poke=id, atk=atk, defense=defense, speed=speed, hp=hp, name=name)
            poke.save()
        else:
            poke = Pokemon.objects.get(id_poke=id)
        return poke