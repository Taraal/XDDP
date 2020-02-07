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

    # Pokemon Team URLs
    path('internal/team/add/', views.addTeam, name='addTeam'),
    path('internal/team/add/pokemon/', views.addPokemonToTeam, name='addPokemonToTeam'),
    path('internal/team/<int:idPlayer>', views.addPokemonToTeam, name='getAllTeamsFromPlayer'),
    path('internal/team/pokemon/<int:idTeam>', views.getPokemonFromTeam, name='getPokemonFromTeam'),

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

    # Setup URLs
    # ATTENTION A NE PAS FLOOD VOTRE BDD#
    path('internal/import/', views.importAll, name='importAll'),
    path('internal/purge/', views.purgeAll, name='purgeAll'),
    # Si erreur : delete db.sqlite3 puis migrate
    ####################################


    # Front URLs
    path('', views.home, name='home'),
    path('Zone1/', views.Zone1, name='Zone1'),
    path('Zone2/', views.Zone2, name='Zone2'),
    path('Zone3/', views.Zone3, name='Zone3'),
    path('Zone4/', views.Zone4, name='Zone4'),
    path('FightPokemon/', views.FightPokemon, name='FightPokemon'),

    # La liaison avec le front-end n'a pas pu être réalisée à temps
    # Pour nous faire pardonner, voici un kangourou en ASCII
    #
    #                                             :e
    #                                            'M$\
    #                                           sf$$br
    #                                         J\J\J$L$L
    #                                       :d  )fM$$$$$r
    #                                  ..P*\ .4MJP   '*\
    #                         sed"""""" ser d$$$F
    #                     .M\  ..JM$$$B$$$$BJ$MR  ...
    #                    dF  nMMM$$$R$$$$$$$h"$ks$$"$$r
    #                  J\.. .MMM8$$$$$LM$P\..'**\    *\
    #                 d :d$r "M$$$$br'$M\d$R
    #                J\MM\ *L   *M$B8MM$B.**
    #               :fd$>  :fhr 'MRM$$M$$"
    #               MJ$>    '5J5..M8$$>
    #              :fMM     d$Fd$$R$$F
    #              4M$P .$$*.J*$$**
    #              M4$> '$>dRdF
    #              MMM\   *L*B.
    #             :$$F     ?k"Re
    #           .$$P\        **'$$B...
    #        :e$F"               '""""


]
