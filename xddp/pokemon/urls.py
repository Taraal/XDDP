from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('all/', views.getAll, name='getAll'),

    #ATTENTION A NE PAS FLOOD VOTRE BDD#
    path('import/', views.importAll, name='importAll')
    ####################################

]