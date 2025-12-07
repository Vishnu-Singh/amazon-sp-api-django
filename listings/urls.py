from django.urls import path
from .views import ListingsItemsView

app_name = 'listings'

urlpatterns = [
    path('<str:seller_id>/<str:sku>/', ListingsItemsView.as_view(), name='listings-item'),
]
