# Generated by Django 4.1 on 2022-09-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0041_delete_subscribe_product_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
