from django.urls import path
from .views import FulfillmentOrdersView, FulfillmentOrderView

app_name = 'fulfillment_outbound'

urlpatterns = [
    path('orders/', FulfillmentOrdersView.as_view(), name='orders-list'),
    path('orders/<str:order_id>/', FulfillmentOrderView.as_view(), name='order-detail'),
]
