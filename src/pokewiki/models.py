from django.db import models
from django.contrib.auth.models import User

# table for pokemon information
class p_table(models.Model):
    p_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    gen  = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    hp = models.IntegerField(default=0)
    atk = models.IntegerField(default=0)
    spatk = models.IntegerField(default=0)
    df = models.IntegerField(default=0)
    spdf = models.IntegerField(default=0)
    spd = models.IntegerField(default=0)
    rarity = models.IntegerField(default=0) # 0: normal, 1:mythical, 2:legendary
    def __str__(self):
        return self.name

# class type_map(models.Model):
# class ability_map(models.Model):
# class move_map(models.Model):

class team_table(models.Model):
    team_name = models.CharField(max_length=50)
    team_code = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

