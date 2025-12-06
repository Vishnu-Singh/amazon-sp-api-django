from django.urls import path
from .views import InboundShipmentsView, InboundShipmentView

app_name = 'fulfillment_inbound'

urlpatterns = [
    path('shipments/', InboundShipmentsView.as_view(), name='shipments-list'),
    path('shipments/<str:shipment_id>/', InboundShipmentView.as_view(), name='shipment-detail'),
]
