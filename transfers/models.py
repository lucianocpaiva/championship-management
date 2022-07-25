from django.db import models


class Transfer(models.Model):
    id = models.AutoField(primary_key=True)

    player = models.ForeignKey(
        'players.Player', related_name='transfers', on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(
        'teams.Team', related_name='transfers', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    price = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.player.name
