from django.urls import path

from . import views

urlpatterns = [
    path('auth/internal/connect', views.authenticate, name='authenticate'),
    path('', views.index, name='connection')
]