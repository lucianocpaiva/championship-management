# Generated by Django 4.0.5 on 2022-07-22 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_remove_team_players'),
        ('tournaments', '0002_alter_tournament_teams'),
        ('matches', '0007_alter_match_team_away_alter_match_team_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='matches.match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_home',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_team', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='tournaments.tournament'),
        ),
    ]
