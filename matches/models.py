from django.db import models


class Match(models.Model):
    id = models.AutoField(primary_key=True)

    team_home = models.ForeignKey(
        'teams.Team', on_delete=models.SET_NULL, null=True, related_name='home_team')
    team_away = models.ForeignKey(
        'teams.Team', on_delete=models.CASCADE,  related_name='team_away')
    tournament = models.ForeignKey(
        'tournaments.Tournament', on_delete=models.SET_NULL, null=True, related_name='matches')
    date = models.DateField()

    def __str__(self):
        return self.team_home.name + ' vs ' + self.team_away.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)

    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    match = models.ForeignKey(
        'matches.Match', on_delete=models.SET_NULL, null=True, related_name='events')

    def __str__(self):
        return self.title
