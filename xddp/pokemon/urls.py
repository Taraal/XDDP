from django.urls import path

from . import views

urlpatterns = [
    path('internal/', views.getAll, name='getAll'),

    path('internal/<int:idPoke>/', views.getOnePokemon, name='getOnePokemon'),
    path('internal/own/', views.getOwnPokemon, name='getOwnPokes'),
    path('internal/add/', views.addOneRandom, name='addOneRandom'),
    path('internal/encounter/<int:idZone>', views.encounter, name='encounter'),


    #ATTENTION A NE PAS FLOOD VOTRE BDD#
    path('internal/import/', views.importAll, name='importAll'),
    path('internal/purge/', views.purgeAll, name='purgeAll'),
    ####################################
    path('internal/fight/<int:idPokemonAttaquant>/<int:idPokemonDefenseur>/<int:idAttack>/',
         views.doFight, name='doFight'),

    path('internal/player/add/', views.addPlayer, name='addPlayer'),
    path('internal/player/', views.getPlayers, name='getPlayers'),
    path('internal/player/<int:idPlayer>/',
         views.getOnePlayer, name='getOnePlayer'),

    path('internal/inventory/<int:idPlayer>/',
         views.getPlayerInventory, name='getPlayerInventory'),
    path('internal/inventory/add/<int:idPlayer>/<int:idItem>/',
         views.addItem, name='addItem'),
    path('internal/inventory/add/<int:idPlayer>/<int:idItem>/<int:nbrAdd>',
         views.addItems, name='addItems'),
]
