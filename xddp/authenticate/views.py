import hashlib, binascii, os

from django.shortcuts import render
from django.http import HttpResponse

from pokemon.models import Player

# Create your views here.

def insertUser(request):
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

def hashPass(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)

    return (salt + pwdhash).decode('ascii')

def authenticate(request):
    """
    Checks the hash of the input password
    :param username
    :param password
    :return:
    """
    username = request.POST.get("username", "")
    providedPassword = request.POST.get("password", "")
    storedPassword = Player.objects.filter(username=username).values_list("password", flat=True)[0]
    salt = storedPassword[:64]
    storedPassword = storedPassword[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', providedPassword.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == storedPassword