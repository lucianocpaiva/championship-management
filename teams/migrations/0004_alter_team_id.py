# Generated by Django 4.0.5 on 2022-07-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_team_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
