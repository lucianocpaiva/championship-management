# Generated by Django 4.0.5 on 2022-07-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_remove_team_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='founded',
        ),
        migrations.RemoveField(
            model_name='team',
            name='stadium',
        ),
        migrations.AddField(
            model_name='team',
            name='coach',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
