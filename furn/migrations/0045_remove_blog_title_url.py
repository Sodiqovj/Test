# Generated by Django 4.1 on 2022-10-17 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0044_remove_arrival_arrivals_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title_url',
        ),
    ]