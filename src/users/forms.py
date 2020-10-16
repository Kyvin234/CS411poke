from django import forms

class TeamForm(forms.Form):
    pokemon_name = forms.CharField(label='pokemon_name', max_length=100)