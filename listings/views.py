from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

class ListingsItemsView(View):
    """
    Proxy view for Amazon SP-API Listings Items endpoints
    
    The Listings Items API provides CRUD operations for listings on Amazon.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, seller_id, sku, *args, **kwargs):
        """Get a listing item"""
        params = {
            'marketplaceIds': request.GET.get('marketplaceIds'),
            'includedData': request.GET.get('includedData'),
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.get(f'/listings/2021-08-01/items/{seller_id}/{sku}', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))
    
    def put(self, request, seller_id, sku, *args, **kwargs):
        """Create or update a listing"""
        try:
            data = json.loads(request.body) if request.body else {}
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        params = {
            'marketplaceIds': request.GET.get('marketplaceIds'),
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.put(f'/listings/2021-08-01/items/{seller_id}/{sku}', data=data, params=params)
        return JsonResponse(response, status=response.get('status_code', 200))
    
    def delete(self, request, seller_id, sku, *args, **kwargs):
        """Delete a listing"""
        params = {
            'marketplaceIds': request.GET.get('marketplaceIds'),
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.delete(f'/listings/2021-08-01/items/{seller_id}/{sku}', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))
    
    def patch(self, request, seller_id, sku, *args, **kwargs):
        """Partially update a listing"""
        try:
            data = json.loads(request.body) if request.body else {}
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        params = {
            'marketplaceIds': request.GET.get('marketplaceIds'),
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.patch(f'/listings/2021-08-01/items/{seller_id}/{sku}', data=data, params=params)
        return JsonResponse(response, status=response.get('status_code', 200))

