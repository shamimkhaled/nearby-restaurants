from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    opening_hour = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=17)
    longitude = models.DecimalField(max_digits=20, decimal_places=17)
    
    
    def __str__(self):
        return self.name
