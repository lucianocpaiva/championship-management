# Generated by Django 4.0.5 on 2022-07-16 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_remove_team_players'),
        ('players', '0004_alter_player_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teams.team'),
        ),
    ]