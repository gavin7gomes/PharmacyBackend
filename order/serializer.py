from rest_framework import serializers
from order.models import Order, OrderItems

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'orderId', 'buyer', 'firstName', 'lastName', 'phone', 'address', 'city', 'pin', 'country', 'paymentMethod', 'amountPayable', 'createdAt',)

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ('id', 'order', 'product', 'quantity')