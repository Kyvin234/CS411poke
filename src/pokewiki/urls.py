from django.urls import path
from . import views
from .views import s_lview, s_dview, a_lview, a_dview
urlpatterns = [
    path('', views.home, name='home'),
    path('pokedex/', s_lview.as_view(), name='pokedex'),
    path('pokedex/pokemon/<str:pk>', s_dview.as_view(), name='pokemon-detail'),
    path('ability-dex/', a_lview.as_view(), name='ability-dex'),
    path('ability-dex/ability/<int:pk>', a_dview.as_view(), name='ability-detail'),
    path('movedex/', views.movedex, name='movedex')
]