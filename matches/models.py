from django.db import models


class Match(models.Model):
    id = models.AutoField(primary_key=True)
    
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='team')
    team_adversary = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='team_adversary')
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE, related_name='tournament', null=False)
    date = models.DateField()

    def __str__(self):
        return self.team.name + ' vs ' + self.team_adversary.name 
