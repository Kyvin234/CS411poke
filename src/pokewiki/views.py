from django.shortcuts import render
from django.db import connection


# Create your views here.
poke_entry = [{
    'p_id' : 1,
    'name' : "bulbsaur",
    'gen'  : 1,
    'img'  : "xxx",
    'type1': "grass",
    'type2': "poison"
},
{
    'p_id' : 2,
    'name' : "ivybsaur",
    'gen'  : 1,
    'img'  : "xxxx",
    'type1': "grass",
    'type2': "poison"

}]
# home page of our pokewiki
def home(request):
    return render(request, 'pokewiki/home.html')
# pokedex part of our pokewiki
def pokedex(request):
    # cursor = connection.cursor()
    # cursor.execute('''
    #     SELECT p_id, name, gen, type1, type2, 
    #     FROM pokewiki_p_table
    # '''
    # )
    data = {
        'poke_entry' : poke_entry
    }
    return render(request, 'pokewiki/pokedex.html', data)
# movedex part of our pokewiki
def movedex(request):
    return render(request, 'pokewiki/movedex.html')

# def pokeinfo(request):
#     return render(request, 'pokewiki/pokeinfo.html')
