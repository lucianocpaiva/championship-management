# Generated by Django 4.0.5 on 2022-07-16 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_remove_player_team'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='players.player'),
        ),
    ]
