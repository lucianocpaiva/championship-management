# Generated by Django 4.0.5 on 2022-07-23 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_alter_tournament_teams'),
        ('matches', '0009_alter_event_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_matches', to='tournaments.tournament'),
        ),
    ]