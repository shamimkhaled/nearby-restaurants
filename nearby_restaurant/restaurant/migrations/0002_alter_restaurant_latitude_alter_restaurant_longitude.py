# Generated by Django 4.2.7 on 2023-11-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.DecimalField(decimal_places=17, max_digits=20),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.DecimalField(decimal_places=17, max_digits=20),
        ),
    ]
