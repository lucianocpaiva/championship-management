# Generated by Django 4.0.5 on 2022-06-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=255)),
                ('founded', models.IntegerField()),
                ('stadium', models.CharField(max_length=255)),
            ],
        ),
    ]
