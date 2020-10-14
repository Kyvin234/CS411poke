from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pokedex/', views.pokedex, name='pokedex'),
    path('movedex/', views.movedex, name='movedex')
]