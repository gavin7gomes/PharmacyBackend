from rest_framework import generics
from products.models import Products
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()