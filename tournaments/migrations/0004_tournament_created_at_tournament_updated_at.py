# Generated by Django 4.0.5 on 2022-07-25 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_alter_tournament_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
