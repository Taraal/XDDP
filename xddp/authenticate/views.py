import hashlib, binascii, os

from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from pokemon.models import Player


def hashPass(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)

    return (salt + pwdhash).decode('ascii')

@csrf_exempt
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

@csrf_exempt
def index(request):
    context = { 'connect' : 'connection'}
    return render(request, "connection.html", context)

@csrf_exempt
def register(request):
    context = { 'register' : 'registration'}
    return render(request, "registration.html", context)