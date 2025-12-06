from django.urls import path
from .views import FeesEstimateView

app_name = 'product_fees'

urlpatterns = [
    path('feesEstimate/', FeesEstimateView.as_view(), name='fees-estimate'),
]
