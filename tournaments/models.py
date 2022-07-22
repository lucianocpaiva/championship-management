from django.db import models


class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=100)
    date = models.DateField()

    teams = models.ManyToManyField('teams.Team', null=True)

    def __str__(self):
        return self.name 


