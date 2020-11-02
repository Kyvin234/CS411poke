from django.shortcuts import render
from .models import s_table, f_table, a_table, a_relation, m_table, m_relation, i_table
from django.views.generic import ListView, DetailView
from django.db import connection


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
#     cursor = connection.cursor()
#     cursor.execute('''
#         SELECT p_id, name, gen, type1, type2, 
#         FROM pokewiki_p_table
#     '''
#     )
    # data = {
    #     'poke_entry' : p_table.objects.all()
    # }
#     return render(request, 'pokewiki/pokedex.html', data)
    
class s_lview(ListView):
    model = s_table
    template_name = 'pokewiki/pokedex.html'
    context_object_name = 'poke_entry'
    # ordering = ['dex_id']
    def get_queryset(self):
        qs = super().get_queryset() 
        return qs.raw("""   SELECT distinct s_name, f_name, dex_id, gen, type1, type2
                            FROM pokewiki_s_table, pokewiki_f_table
                            WHERE s_name = s_name_id 
                            ORDER BY dex_id
                      """)

class s_dview(DetailView):
    model = s_table
    def get_context_data(self, **kwargs):
    # get context from the class this very function belongs to
        context = super().get_context_data(**kwargs)
        cursor = connection.cursor()
        cursor.execute('''
                        SELECT * 
                        FROM pokewiki_f_table AS pf 
                             JOIN pokewiki_s_table AS ps ON pf.s_name_id = ps.s_name
                        WHERE s_name = %s
                           ''' , (self.kwargs['pk'],)) 
        context['pokemon_detail'] = dictfetchall(cursor)
        cursor.execute('''
                SELECT f_name, a_id, a_name, is_hidden
                FROM pokewiki_f_table AS pf 
                        JOIN pokewiki_s_table AS ps ON pf.s_name_id = ps.s_name
                        JOIN pokewiki_a_relation AS ar ON ar.f_name_id = pf.f_name
                        NATURAL JOIN pokewiki_a_table
                WHERE s_name = %s
                    ''' , (self.kwargs['pk'],))
        context['pokemon_ability'] = dictfetchall(cursor)
        cursor.execute('''
                SELECT f_name_id, m_name_id
                FROM pokewiki_m_relation
                WHERE f_name_id LIKE %s
                order by f_name_id
                    ''' , (''+self.kwargs['pk']+'%',))
        context['pokemon_move'] = dictfetchall(cursor)
        return context

class a_lview(ListView):
    model = a_table
    template_name = 'pokewiki/abidex.html'
    context_object_name = 'ability_entry'

class a_dview(DetailView):
    model = a_table
    def get_context_data(self, **kwargs):
    # get context from the class this very function belongs to
        context = super().get_context_data(**kwargs)
        cursor = connection.cursor()
        cursor.execute('''
                          SELECT f_name_id, s_name_id, count, is_hidden
                          FROM pokewiki_a_table NATURAL JOIN pokewiki_a_relation as AR NATURAL JOIN (
                              SELECT count(*) as count
                              FROM pokewiki_a_table NATURAL JOIN pokewiki_a_relation 
                              WHERE a_id = %s
                              GROUP BY a_id
                          ) as t1 JOIN pokewiki_f_table as FT ON AR.f_name_id = FT.f_name
                          WHERE a_id = %s ''' , (self.kwargs['pk'],self.kwargs['pk'])) 
        context['p_with_a'] = dictfetchall(cursor)
        return context

# movedex part of our pokewiki
class m_lview(ListView):
    model = m_table
    template_name = 'pokewiki/movedex.html'
    context_object_name = 'move_entry'
    ordering = ['m_id']

class m_dview(DetailView):
    model = m_table
    def get_context_data(self, **kwargs):
    # get context from the class this very function belongs to
        context = super().get_context_data(**kwargs)
        cursor = connection.cursor()
        cursor.execute('''
                          SELECT distinct s_name, f_name, dex_id, type1, type2, count, mr.gen
                          FROM pokewiki_m_table AS mt JOIN (SELECT distinct s_name, m_name_id, dex_id, type1, type2, f_name, st.gen
                                                            FROM pokewiki_m_relation AS mr2 JOIN 
                                                                 pokewiki_f_table AS ft ON mr2.f_name_id = ft.f_name JOIN
                                                                 pokewiki_s_table AS st ON ft.s_name_id = st.s_name
                                                            WHERE m_name_id = %s) AS mr ON mt.m_name = mr.m_name_id 
                                                      JOIN  (SELECT count(*) as count, m_name_id
                                                             FROM pokewiki_m_relation
                                                             WHERE m_name_id = %s
                                                             GROUP BY m_name_id) AS ct    
                                                      ORDER BY dex_id               
                           ''' , (self.kwargs['pk'],self.kwargs['pk'])) 
        context['p_with_m'] = dictfetchall(cursor)
        return context

class i_lview(ListView):
    model = i_table
    template_name = 'pokewiki/itemdex.html'
    context_object_name = 'item_entry'

class i_dview(DetailView):
    model = i_table

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]