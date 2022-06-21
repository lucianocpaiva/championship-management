# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from teams.models import Team

class Player(models.Model):
    name = models.CharField(max_length=30)
    birth = models.DateField(blank=False)
    country = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

