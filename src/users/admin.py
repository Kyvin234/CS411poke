from django.contrib import admin
from .models import profile_table, team_table

# Register your models here.
admin.site.register(profile_table)
admin.site.register(team_table)
