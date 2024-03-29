from django.db import models

from teams.models import Team


class Player(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=30)
    birth = models.DateField(blank=False)
    country = models.CharField(max_length=30)

    team = models.ForeignKey(
        Team, null=True, related_name='players', on_delete=models.SET_NULL)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
