# Generated by Django 4.1.7 on 2023-03-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annote',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
