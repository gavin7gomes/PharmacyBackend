from django.urls import path

from order import views


app_name = "order"

urlpatterns = [
    path("", views.OrderList.as_view(), name='order'),
    path("<int:pk>", views.OrderDetails.as_view(), name='orderDetails'),
    path("items", views.CreateOrderItems.as_view(), name='orderItems'),
     path("items/<int:order>", views.GetOrderItems.as_view(), name='orderItemsByOrderId'),
]