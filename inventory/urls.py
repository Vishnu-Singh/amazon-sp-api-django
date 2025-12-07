from django.urls import path
from .views import InventorySummariesView

app_name = 'inventory'

urlpatterns = [
    path('summaries/', InventorySummariesView.as_view(), name='inventory-summaries'),
]
