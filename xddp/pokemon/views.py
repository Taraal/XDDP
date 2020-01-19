import json

from django.http import HttpResponse
from .models import Pokemon

from django.core import serializers


def Home(request):
    """
    To be deleted
    """
    return HttpResponse("Hi")


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
