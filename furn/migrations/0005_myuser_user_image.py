# Generated by Django 4.0.4 on 2022-07-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0004_arrival_arrivals_text_arrival_arrvals_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]