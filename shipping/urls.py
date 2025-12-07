from django.urls import path
from .views import ShippingView, TrackingView

app_name = 'shipping'

urlpatterns = [
    path('shipments/', ShippingView.as_view(), name='shipping'),
    path('tracking/<str:tracking_id>/', TrackingView.as_view(), name='tracking'),
]
