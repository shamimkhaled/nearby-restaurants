# Generated by Django 4.2.7 on 2023-11-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurants_delete_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='open_hour',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
