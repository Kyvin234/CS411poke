from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.views.generic import ListView
from .forms import TeamForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
    
@login_required
def team(request):
    # HTML contains a cascading dropdown selecting list
    # If a form is submitted, reload page and hide the form
    if request.method == 'POST':
        form = TeamForm(request.POST)
        # if form.is_valid():
        #     # form.save()
        #     username = form.cleaned_data.get('username')
        t_name = form.cleaned_data.get('teamname')
        messages.success(request, f'team created {t_name}!')
        return redirect('team')
    else:
        form = TeamForm()
    return render(request, 'users/team.html', {'form': form})

# def teamListView()