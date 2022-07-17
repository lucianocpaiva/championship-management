# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from players.models import Player

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=255)
    founded = models.IntegerField()
    stadium = models.CharField(max_length=255)

    # players = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='teams')    

    def __str__(self):
        return self.name

    
