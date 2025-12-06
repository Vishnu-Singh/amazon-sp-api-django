from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

class OrdersView(View):
    """
    Proxy view for Amazon SP-API Orders endpoints
    
    The Orders API helps you retrieve order information.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, *args, **kwargs):
        """
        Get orders
        
        Query Parameters:
            - marketplaceIds: A list of marketplace identifiers
            - createdAfter: Orders created after this timestamp
            - createdBefore: Orders created before this timestamp
            - lastUpdatedAfter: Orders last updated after this timestamp
            - orderStatuses: A list of OrderStatus values
            - fulfillmentChannels: A list of FulfillmentChannel values
            - maxResultsPerPage: Maximum number of orders to return
        """
        params = {
            'marketplaceIds': request.GET.get('marketplaceIds'),
            'createdAfter': request.GET.get('createdAfter'),
            'createdBefore': request.GET.get('createdBefore'),
            'lastUpdatedAfter': request.GET.get('lastUpdatedAfter'),
            'orderStatuses': request.GET.get('orderStatuses'),
            'fulfillmentChannels': request.GET.get('fulfillmentChannels'),
            'maxResultsPerPage': request.GET.get('maxResultsPerPage', 100),
        }
        
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.get('/orders/v0/orders', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))


class OrderView(View):
    """Get a specific order by ID"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, order_id, *args, **kwargs):
        """Get order details"""
        response = self.client.get(f'/orders/v0/orders/{order_id}')
        return JsonResponse(response, status=response.get('status_code', 200))


class OrderItemsView(View):
    """Get order items for a specific order"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, order_id, *args, **kwargs):
        """Get order items"""
        params = {
            'nextToken': request.GET.get('nextToken'),
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.get(f'/orders/v0/orders/{order_id}/orderItems', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))

