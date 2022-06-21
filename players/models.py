# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)
    birth = models.DateField(blank=False)
    country = models.CharField(max_length=30)
    team = models.CharField(max_length=30)

