from django.urls import path

from . import views

urlpatterns = [
    path('internal/', views.getAll, name='getAll'),

    path('internal/<int:idPoke>/', views.getOnePokemon, name='getOnePokemon'),
    path('internal/own/', views.getOwnPokemon, name='getOwnPokes'),
    path('internal/add/', views.addOneRandom, name='addOneRandom'),

    #ATTENTION A NE PAS FLOOD VOTRE BDD#
    path('internal/import/', views.importAll, name='importAll'),
    ####################################

    path('internal/player/add/', views.addPlayer, name='addPlayer'),
    path('internal/player/', views.getPlayers, name='getPlayers'),
    path('internal/player/<int:idPlayer>/', views.getOnePlayer, name='getOnePlayer'),



]