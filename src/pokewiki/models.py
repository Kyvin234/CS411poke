from django.db import models
# from django.contrib.auth.models import User

# types
class t_table(models.Model):
    t_name = models.CharField(primary_key=True, max_length=10, default="")
    t_id = models.IntegerField(default=0)

# types relations
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

# pokemon species
class s_table(models.Model):
    s_name = models.CharField(primary_key=True, max_length=50)
    dex_id = models.IntegerField(default=0)
    gen  = models.IntegerField(default=0)
    gender_rate = models.IntegerField(default=0, null=True)
    capture_rate = models.IntegerField(default=0, null=True)
    
# pokemon forms
class f_table(models.Model):
    f_name = models.CharField(primary_key=True, max_length=50)
    s_name = models.ForeignKey(s_table, on_delete=models.CASCADE)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    hp = models.IntegerField(default=0, null=True)
    atk = models.IntegerField(default=0, null=True)
    df = models.IntegerField(default=0, null=True)
    spatk = models.IntegerField(default=0, null=True)
    spdf = models.IntegerField(default=0, null=True)
    spd = models.IntegerField(default=0, null=True)
    type1 = models.CharField(default="", max_length=10)
    type2 = models.CharField(default="", max_length=10)

# abilities
class a_table(models.Model):
    a_id = models.IntegerField(primary_key=True)
    a_name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)

# pokemon forms that have the relations 
class a_relation(models.Model):
    f_name = models.ForeignKey(f_table, on_delete=models.CASCADE)
    a = models.ForeignKey(a_table, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=True)

# moves
class m_table(models.Model):
    m_name = models.CharField(primary_key=True, max_length=50)
    m_id = models.IntegerField(default=0)
    pp = models.IntegerField(default=0, null=True)
    power = models.IntegerField(default=0, null=True)
    accuaracy = models.IntegerField(default=0, null=True)
    priority = models.IntegerField(default=0, null=True)
    types = models.CharField(default='', max_length=10, null=True)
    dmg_class = models.CharField(default='', max_length=10, null=True)
    effect = models.CharField(default='', max_length=3500, null=True)
    gen = models.IntegerField(default=0, null=True)
# class i_table(models.Model):
class m_relation(models.Model):
    m_name = models.ForeignKey(m_table, on_delete=models.CASCADE, default='')
    f_name = models.ForeignKey(f_table, on_delete=models.CASCADE, default='')
    # learn_method = models.CharField(default="", max_length=10)
    # level_learned = models.IntegerField(default=0)

# class n_table(models.Model):




