# Generated by Django 5.0.1 on 2024-01-20 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_votes_datetime_alter_votes_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 21, 1, 22, 20, 251005)),
        ),
    ]
