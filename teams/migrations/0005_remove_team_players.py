# Generated by Django 4.0.5 on 2022-07-16 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_alter_team_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
    ]
