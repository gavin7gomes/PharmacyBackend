from dataclasses import field, fields
from rest_framework import serializers
from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'brand', 'description', 'price', 'in_stock', 'ratings', 'supplier', 'needs_prescription', 'image', 'listed_on')