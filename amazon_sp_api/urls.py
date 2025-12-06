"""
URL configuration for amazon_sp_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    """Root API endpoint showing all available endpoints"""
    return JsonResponse({
        'message': 'Amazon SP-API Django Integration',
        'version': '1.0.0',
        'endpoints': {
            'feeds': '/api/feeds/',
            'catalog': '/api/catalog/',
            'orders': '/api/orders/',
            'listings': '/api/listings/',
            'reports': '/api/reports/',
            'fulfillment_inbound': '/api/fulfillment-inbound/',
            'fulfillment_outbound': '/api/fulfillment-outbound/',
            'merchant_fulfillment': '/api/merchant-fulfillment/',
            'finance': '/api/finance/',
            'product_pricing': '/api/product-pricing/',
            'product_fees': '/api/product-fees/',
            'sellers': '/api/sellers/',
            'inventory': '/api/inventory/',
            'shipping': '/api/shipping/',
            'notifications': '/api/notifications/',
            'authorization': '/api/authorization/',
            'small_and_light': '/api/small-and-light/',
            'tokens': '/api/tokens/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/feeds/', include('feeds.urls')),
    path('api/catalog/', include('catalog.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/listings/', include('listings.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/fulfillment-inbound/', include('fulfillment_inbound.urls')),
    path('api/fulfillment-outbound/', include('fulfillment_outbound.urls')),
    path('api/merchant-fulfillment/', include('merchant_fulfillment.urls')),
    path('api/finance/', include('finance.urls')),
    path('api/product-pricing/', include('product_pricing.urls')),
    path('api/product-fees/', include('product_fees.urls')),
    path('api/sellers/', include('sellers.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/shipping/', include('shipping.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/authorization/', include('authorization.urls')),
    path('api/small-and-light/', include('small_and_light.urls')),
    path('api/tokens/', include('tokens.urls')),
]
