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
    ####################################

    path('internal/player/add/', views.addPlayer, name='addPlayer'),
    path('internal/player/', views.getPlayers, name='getPlayers'),
    path('internal/player/<int:idPlayer>/', views.getOnePlayer, name='getOnePlayer'),



    path('', views.home, name='home'),
    path('Zone1/', views.Zone1, name='Zone1'),
    path('Zone2/', views.Zone2, name='Zone2'),
    path('Zone3/', views.Zone3, name='Zone3'),
    path('Zone4/', views.Zone4, name='Zone4'),
]