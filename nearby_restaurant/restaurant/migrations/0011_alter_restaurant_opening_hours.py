# Generated by Django 4.2.7 on 2023-11-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_alter_restaurant_opening_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='opening_hours',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
