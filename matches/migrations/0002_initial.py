# Generated by Django 4.0.5 on 2022-07-25 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tournaments', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tournament_matches', to='tournaments.tournament'),
        ),
        migrations.AddField(
            model_name='event',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_events', to='matches.match'),
        ),
    ]
