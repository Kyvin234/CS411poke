from django.shortcuts import render
from .models import p_table
from django.views.generic import ListView, DetailView
# from django.db import connection


# Create your views here.
# poke_entry = [{
#     'p_id' : 1,
#     'name' : "bulbsaur",
#     'gen'  : 1,
#     'img'  : "xxx",
#     'type1': "grass",
#     'type2': "poison"
# },
# {
#     'p_id' : 2,
#     'name' : "ivybsaur",
#     'gen'  : 1,
#     'img'  : "xxxx",
#     'type1': "grass",
#     'type2': "poison"

# }]
# home page of our pokewiki
def home(request):
    return render(request, 'pokewiki/home.html')
# pokedex part of our pokewiki
# def pokedex(request):
    # cursor = connection.cursor()
    # cursor.execute('''
    #     SELECT p_id, name, gen, type1, type2, 
    #     FROM pokewiki_p_table
    # '''
    # )
    # data = {
    #     'poke_entry' : p_table.objects.all()
    # }
    # return render(request, 'pokewiki/pokedex.html', data)
    
class pokelistview(ListView):
    model = p_table
    template_name = 'pokewiki/pokedex.html'
    context_object_name = 'poke_entry'

class pokedetailview(DetailView):
    model = p_table

# movedex part of our pokewiki
def movedex(request):
    return render(request, 'pokewiki/movedex.html')

# def pokeinfo(request):
#     return render(request, 'pokewiki/pokeinfo.html')
