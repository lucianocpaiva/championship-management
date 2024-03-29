# Generated by Django 4.0.5 on 2022-07-22 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_alter_match_tournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='matches.match')),
            ],
        ),
    ]
