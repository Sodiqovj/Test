# Generated by Django 4.1 on 2022-09-16 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0035_rename_rate_1_product_rating_remove_product_rate_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='secret',
            field=models.CharField(default='null_undefined', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(default='2', max_length=10),
        ),
    ]