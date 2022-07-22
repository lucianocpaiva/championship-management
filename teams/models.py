from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=255)
    founded = models.IntegerField()
    stadium = models.CharField(max_length=255)

    def __str__(self):
        return self.name
