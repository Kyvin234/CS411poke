from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.views.generic import ListView, CreateView, DeleteView
from .models import team_table
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
import json
# from .forms import TeamForm

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
    
@method_decorator(login_required, name='dispatch')
class team_lview(ListView):
    model = team_table
    template_name = 'users/team.html'
    context_object_name = 'team_entry'
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.raw("""   SELECT *
                            FROM users_team_table
                            WHERE creator_id = %s
                        """, (self.request.user.id,))

@method_decorator(login_required, name='dispatch')
class team_cview(CreateView):
    model = team_table
    fields = ['team_name', 'team_comp', 'description']  
    success_url = reverse_lazy('team')
    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users_team_table(team_name,team_comp,creator_id,description) VALUES( %s , %s , %s, %s)", 
            [form.instance.team_name, json.dumps(form.instance.team_comp), form.instance.creator_id, form.instance.description]
        )
        return HttpResponseRedirect(self.success_url) 

@method_decorator(login_required, name='dispatch')
class team_delview(CreateView):
    model = team_table
    success_url = reverse_lazy('team')
    def delete(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # self.object.delete()
        cursor = connection.cursor()
        cursor.execute(
            """ DELETE
                FROM users_team_table
                WHERE id = %s
            """, (self.kwargs['pk'], )
        )
        return HttpResponseRedirect(self.success_url)
    def get(self, *a, **kw):
        return self.delete(*a, **kw)


# def team(request):
    # HTML contains a cascading dropdown selecting list
    # If a form is submitted, reload page and hide the form
    # if request.method == 'POST':
    #     form = TeamForm(request.POST)
    #     # if form.is_valid():
    #     #     # form.save()
    #     #     username = form.cleaned_data.get('username')
    #     t_name = form.cleaned_data.get('teamname')
    #     messages.success(request, f'team created {t_name}!')
    #     return redirect('team')
    # else:
    #     form = TeamForm()
    # # print(team_table.objects.all())
    # data = {
    #     'team_entry' : team_table.objects.all()
    # }
    # return render(request, 'users/team.html', data)

# def teamListView()