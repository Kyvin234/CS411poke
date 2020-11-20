from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import team_table
from pokewiki.models import f_table
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import teamform
import json
import pymongo


# mongodb clients
myclient = pymongo.MongoClient("mongodb+srv://yuey8:yuyue72520@cluster0-t2jyv.mongodb.net/Student_Info?retryWrites=true&w=majority")
mydb = myclient['cs411']

# register form
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
# user profile form
@login_required
def profile(request):
    return render(request, 'users/profile.html')
# user's team view
class team_lview(LoginRequiredMixin, ListView):
    model = team_table
    template_name = 'users/team.html'
    context_object_name = 'team_entry'
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.raw("""   SELECT *
                            FROM users_team_table
                            WHERE creator_id = %s
                        """, (self.request.user.id,))
# user team-creating view
class team_cview(LoginRequiredMixin, CreateView):
    model = team_table
    fields = ['team_name', 'team_comp','description']  
    success_url = reverse_lazy('team')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # item detail
        cursor = connection.cursor()
        cursor.execute('''
                            SELECT i_name
                            FROM pokewiki_i_table
                            ORDER BY category
                           ''') 
        context['item_info'] = dictfetchall(cursor)
        # pokemon detail(mongodb team data)
        mycol = mydb['gen7ou']
        x = list(mycol.find().sort("dex_id"))
        context['pokemon_team_detail'] = {'pokemon_team_detail' : x}
        return context
    
    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users_team_table(team_name,team_comp,creator_id,description) VALUES(%s, %s, %s, %s)", 
            [form.instance.team_name, json.dumps(form.instance.team_comp), form.instance.creator_id, form.instance.description]
        )
        return HttpResponseRedirect(self.success_url)
# user team-deleating view
class team_delview(LoginRequiredMixin, UserPassesTestMixin, CreateView):
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
    def test_func(self):
        post = self.get_object()
        if(self.request.user.id == post.creator_id):
            return True
        else:
            return False
# user team updating view
class team_uview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = team_table
    fields = ['team_name', 'team_comp', 'description']  
    success_url = reverse_lazy('team')
    def get_context_data(self, **kwargs):
        mycol = mydb['gen7ou']
        x = list(mycol.find().sort("dex_id"))
        # user's team info
        context = super().get_context_data(**kwargs)
        # cursor = connection.cursor()
        # cursor.execute('''
        #                  SELECT distinct s_name, f_name, dex_id, gen, type1, type2
        #                     FROM pokewiki_s_table, pokewiki_f_table
        #                     WHERE s_name = s_name_id 
        #                     ORDER BY dex_id
        #                    ''') 
        # context['pokemon_detail'] = dictfetchall(cursor)
        context['pokemon_team_detail'] = {'pokemon_team_detail' : x}
        return context
        
    def post(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute(
            '''UPDATE users_team_table 
               SET team_name=%s, team_comp=%s, description=%s
               WHERE id = %s
            ''', 
            [request.POST.get('team_name'), request.POST.get('team_comp'), request.POST.get('description'), self.kwargs['pk']]
        )
        return HttpResponseRedirect(self.success_url) 
    def test_func(self):
        post = self.get_object()
        if(self.request.user.id == post.creator_id):
            return True
        else:
            return False

# ajax requests
def get_pokeinfo(request):
    pokemon = request.POST.get("pokemon")
    cursor = connection.cursor()
    cursor.execute(
        
            """ SELECT a_name
                FROM pokewiki_f_table AS pf 
                        JOIN pokewiki_a_relation AS ar ON ar.f_name_id = pf.f_name
                        NATURAL JOIN pokewiki_a_table
                WHERE f_name = %s
            """, (pokemon, )
    )
    ability =  dictfetchall(cursor)
    data = {
        "ability" : ability,
    } 
    return JsonResponse(data)

# converting mysql cursor into a dictionary for django template language access
def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
