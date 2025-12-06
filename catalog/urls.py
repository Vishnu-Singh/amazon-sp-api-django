from django.urls import path
from .views import CatalogItemsView, CatalogItemView

app_name = 'catalog'

urlpatterns = [
    path('', CatalogItemsView.as_view(), name='catalog-items-search'),
    path('<str:asin>/', CatalogItemView.as_view(), name='catalog-item-detail'),
]
