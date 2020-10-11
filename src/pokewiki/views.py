from django.shortcuts import render
# Create your views here.

# home page of our pokewiki
def home(request):
    return render(request, 'pokewiki/home.html')
# pokedex part of our pokewiki
def pokemon(request):
    return render(request, 'pokewiki/pokemon.html')
# movedex part of our pokewiki
def move(request):
    return render(request, 'pokewiki/move.html')
