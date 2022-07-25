from django.db import models


class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    teams = models.ManyToManyField('teams.Team', through='TournamentTeam')
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class TournamentTeam(models.Model):
    id = models.AutoField(primary_key=True)
    tournament = models.ForeignKey('Tournament', on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.tournament.name + ' - ' + self.team.name
    
    class Meta:
        unique_together = ('team', 'tournament',)