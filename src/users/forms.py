from django import forms
from pokewiki.models import p_table


FAVORITE_POKEMON = [
    ('Bulbsaur', 'bulbsaur'), ('Riolu', 'riolu')
]
FAVORITE_NATURE = [
    ('Jolly', 'jolly'), ('Lax', 'lax')
]
class TeamForm(forms.Form):
    teamname = forms.CharField(label='team', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Team Name'}))
    pokemon  = forms.CharField(required=True, widget=forms.Select(choices=FAVORITE_POKEMON))
    nature   = forms.CharField(required=True, widget=forms.Select(choices=FAVORITE_NATURE))
    