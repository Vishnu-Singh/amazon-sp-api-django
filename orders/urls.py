from django.urls import path
from .views import OrdersView, OrderView, OrderItemsView

app_name = 'orders'

urlpatterns = [
    path('', OrdersView.as_view(), name='orders-list'),
    path('<str:order_id>/', OrderView.as_view(), name='order-detail'),
    path('<str:order_id>/items/', OrderItemsView.as_view(), name='order-items'),
]
