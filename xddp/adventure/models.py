from django.db import models

from pokemon.models import Pokemon

class Zone(models.Model):

    name = models.TextField(null=True)
    min_level = models.IntegerField(null=True)
    max_level = models.IntegerField(null=True, default=(min_level + 10))
    allowed_pokemon = models.ManyToManyField(Pokemon)

    def __str__(self):
        return self.name
