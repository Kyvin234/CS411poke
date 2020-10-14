from django.shortcuts import render
# Create your views here.
poke_entry = [{
    'p_id' : 1,
    'name' : "bulbsaur",
    'gen'  : 1,
    'img'  : "xxx"
},
{
    'p_id' : 2,
    'name' : "ivybsaur",
    'gen'  : 1,
    'img'  : "xxxx"
}]
# home page of our pokewiki
def home(request):
    return render(request, 'pokewiki/home.html')
# pokedex part of our pokewiki
def pokedex(request):
    data = {
        'poke_entry' : poke_entry
    }
    return render(request, 'pokewiki/pokedex.html', data)
# movedex part of our pokewiki
def movedex(request):
    return render(request, 'pokewiki/movedex.html')
