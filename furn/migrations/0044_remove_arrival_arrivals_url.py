# Generated by Django 4.1 on 2022-10-17 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0043_carousel_aboute_en_carousel_aboute_uz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrival',
            name='arrivals_url',
        ),
    ]