from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import jsonfield

from products.models import Products

class Order(models.Model):
    orderId = models.CharField(max_length=200)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    country = models.CharField(max_length=20)
    paymentMethod = models.CharField(max_length=20)
    amountPayable = models.DecimalField(max_digits=10, decimal_places=1)
    createdAt = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.orderId

class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    def __str__(self):
        return self.order