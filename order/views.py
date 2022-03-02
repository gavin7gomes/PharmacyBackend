from rest_framework import generics

from order.models import Order, OrderItems
from order.serializer import OrderSerializer, OrderListSerializer

class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(buyer=user)

class CreateOrderItems(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderListSerializer

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class GetOrderItems(generics.ListAPIView):
    serializer_class = OrderListSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        order = self.kwargs['order']
        return OrderItems.objects.filter(order=order)