# Generated by Django 5.0.1 on 2024-01-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_votes_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='category',
        ),
        migrations.AlterField(
            model_name='votes',
            name='datetime',
            field=models.DateTimeField(default='21/01/2024, 01:16:51'),
        ),
    ]