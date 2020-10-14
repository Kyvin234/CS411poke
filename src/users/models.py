from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile_table(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_poke = models.name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username} Profile'

class team_table(models.Model):
    team_name = models.CharField(max_length=50)
    team_code = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "%s : %s" % (self.creator, self.team_name)

        