from django.urls import path

from . import views

urlpatterns = [
    path('', views.authenticate, name='authenticate'),
]