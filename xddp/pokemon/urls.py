from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.getAll, name='getAll'),

    #ATTENTION A NE PAS FLOOD VOTRE BDD#
    #path('import/', views.importAll, name='importAll'),
    ####################################

    path('add/', views.addOneRandom, name='addOneRandom'),

    #URLs for testing purposes
    path('addplayer/', views.addPlayer, name='addPlayer'),
    path('getplayers/', views.getPlayers, name='getPlayers'),
    path('getownpokes/', views.getOwnPokemon, name='getOwnPokes'),

    path('', views.home, name='home'),
    path('Zone1/', views.Zone1, name='Zone1'),
    path('Zone2/', views.Zone2, name='Zone2'),
    path('Zone3/', views.Zone3, name='Zone3'),
    path('Zone4/', views.Zone4, name='Zone4'),
]