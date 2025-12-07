from django.urls import path
from .views import SubscriptionsView, DestinationsView

app_name = 'notifications'

urlpatterns = [
    path('subscriptions/<str:notification_type>/', SubscriptionsView.as_view(), name='subscriptions'),
    path('destinations/', DestinationsView.as_view(), name='destinations'),
]
