# Generated by Django 4.2.7 on 2023-11-08 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_alter_restaurant_opening_hours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='opening_hours',
        ),
    ]