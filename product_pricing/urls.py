from django.urls import path
from .views import PricingView, CompetitivePricingView

app_name = 'product_pricing'

urlpatterns = [
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('competitivePrice/', CompetitivePricingView.as_view(), name='competitive-pricing'),
]
