# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=255)
    founded = models.IntegerField()
    stadium = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    
