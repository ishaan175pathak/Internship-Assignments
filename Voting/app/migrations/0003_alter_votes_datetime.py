# Generated by Django 5.0.1 on 2024-01-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_votes_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='datetime',
            field=models.DateTimeField(default='16/01/2024, 21:28:21'),
        ),
    ]
