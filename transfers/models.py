# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.player.name 




