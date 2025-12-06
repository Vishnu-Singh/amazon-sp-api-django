from django.urls import path
from .views import EligibleShipmentsView, ShipmentsView

app_name = 'merchant_fulfillment'

urlpatterns = [
    path('eligibleShippingServices/', EligibleShipmentsView.as_view(), name='eligible-shipments'),
    path('shipments/', ShipmentsView.as_view(), name='shipments'),
]
