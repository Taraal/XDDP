from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('all/', views.getAll, name='getAll'),

    #ATTENTION A NE PAS FLOOD VOTRE BDD#
    path('import/', views.importAll, name='importAll'),
    ####################################

    path('add/', views.addOneRandom, name='addOneRandom'),

    #URLs for testing purposes
    path('addplayer/', views.addPlayer, name='addPlayer'),
    path('getplayers/', views.getPlayers, name='getPlayers'),
    path('getownpokes/', views.getOwnPokemon, name='getOwnPokes'),

]