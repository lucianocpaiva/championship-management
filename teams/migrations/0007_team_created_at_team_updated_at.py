# Generated by Django 4.0.5 on 2022-07-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_remove_team_founded_remove_team_stadium_team_coach_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
