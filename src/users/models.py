from django.db import models
from django.contrib.auth.models import User
from pokewiki.models import s_table
from django.urls import reverse
# from django_mysql.models import jsonfiel

# Create your models here.
class profile_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user} Profile'

class team_table(models.Model):
    team_name = models.CharField(max_length=50, unique=True)
    team_comp = models.JSONField(null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(default='',max_length=5000)
    def __str__(self):
        return "%s : %s" % (self.creator, self.team_name)
    def get_absolute_url(self):
        return reverse('team')
    

        