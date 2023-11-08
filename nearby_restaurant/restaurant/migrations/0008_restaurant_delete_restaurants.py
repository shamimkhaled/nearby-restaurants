# Generated by Django 4.2.7 on 2023-11-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_alter_restaurants_opening_hours_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('opening_hours', models.JSONField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=17, max_digits=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurants',
        ),
    ]