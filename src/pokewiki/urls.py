from django.urls import path
from . import views
from .views import pokelistview, pokedetailview

urlpatterns = [
    path('', views.home, name='home'),
    path('pokedex/', pokelistview.as_view(), name='pokedex'),
    path('pokedex/pokemon/<int:pk>', pokedetailview.as_view(), name='pokemon-detail'),
    path('movedex/', views.movedex, name='movedex')
]