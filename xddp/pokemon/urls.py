from django.urls import path

from . import views

urlpatterns = [


    # Pokemon URLs
    path('internal/', views.getAll, name='getAll'),
    path('internal/<int:idPoke>/', views.getOnePokemon, name='getOnePokemon'),
    path('internal/own/<int:idPlayer>/', views.getOwnPokemon, name='getOwnPokes'),

    # Ajout des pokémons
    path('internal/add/random/<int:idPlayer>/', views.addOneRandom, name='addOneRandom'),
    path('internal/add/<int:idPoke>/<int:idPlayer>/', views.addOnePokemon, name='addOnePokemon'),

    # Rencontre d'un pokémon par zone
    path('internal/encounter/<int:idZone>', views.encounter, name='encounter'),

    # Fight URLs
    path('internal/fight/<int:idPokemonAttaquant>/<int:idPokemonDefenseur>/<int:idAttack>/',
         views.doFight, name='doFight'),


    # Player URLs
    path('internal/player/add/', views.addPlayer, name='addPlayer'),
    path('internal/player/', views.getPlayers, name='getPlayers'),
    path('internal/player/<int:idPlayer>/',
         views.getOnePlayer, name='getOnePlayer'),


    # Inventory URLs
    path('internal/inventory/<int:idPlayer>/',
         views.getPlayerInventory, name='getPlayerInventory'),
    path('internal/inventory/add/<int:idPlayer>/<int:idItem>/',
         views.addItem, name='addItem'),
    path('internal/inventory/add/<int:idPlayer>/<int:idItem>/<int:nbrAdd>',
         views.addItems, name='addItems'),

    # ATTENTION A NE PAS FLOOD VOTRE BDD#
    path('internal/import/', views.importAll, name='importAll'),
    path('internal/purge/', views.purgeAll, name='purgeAll'),
    # Si erreur : delete db.sqlite3 puis migrate
    ####################################

]
