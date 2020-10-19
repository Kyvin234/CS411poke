from django.db import models
# from django.contrib.auth.models import User


class t_table(models.Model):
    t_name = models.CharField(primary_key=True, max_length=10, default="")
    t_id = models.IntegerField(default=0)

class t_relation(models.Model):
    t = models.OneToOneField(t_table, on_delete=models.CASCADE)
    Normal = models.FloatField(default=0)
    Fire = models.FloatField(default=0)
    Water = models.FloatField(default=0)
    Grass = models.FloatField(default=0)
    Flying = models.FloatField(default=0)
    Fighting = models.FloatField(default=0) 
    Poison = models.FloatField(default=0) 
    Electric = models.FloatField(default=0) 
    Ground = models.FloatField(default=0) 
    Rock = models.FloatField(default=0) 
    Psychic = models.FloatField(default=0) 
    Ice = models.FloatField(default=0) 
    Bug = models.FloatField(default=0) 
    Ghost = models.FloatField(default=0) 
    Steel = models.FloatField(default=0) 
    Dragon = models.FloatField(default=0) 
    Dark  = models.FloatField(default=0)
    Fairy = models.FloatField(default=0)

# table for pokemon information
class p_table(models.Model):
    p_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    hp = models.IntegerField(default=0)
    atk = models.IntegerField(default=0)
    df = models.IntegerField(default=0)
    spatk = models.IntegerField(default=0)
    spdf = models.IntegerField(default=0)
    spd = models.IntegerField(default=0)
    gen  = models.IntegerField(default=0)
    type1 = models.CharField(default="", max_length=10)
    type2 = models.CharField(default="", max_length=10)
    gender_rate = models.IntegerField(default=0)
    capture_rate = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
# class i_table(models.Model):
class a_table(models.Model):
    a_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
# class n_table(models.Model):

# class a_relation(models.Model):
# class m_relation(models.Model):
    # m_id = 




