from django.db import models
from datetime import datetime

class Products(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    in_stock = models.IntegerField()
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    supplier = models.CharField(max_length=200)
    needs_prescription = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/", blank=True)
    listed_on = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name