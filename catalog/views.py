from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

class CatalogItemsView(View):
    """
    Proxy view for Amazon SP-API Catalog Items endpoints
    
    The Catalog Items API helps you search for and retrieve information about items in the Amazon catalog.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, *args, **kwargs):
        """
        Search catalog items
        
        Query Parameters:
            - keywords: Keywords to search for
            - marketplaceIds: A comma-delimited list of marketplace identifiers
            - identifiers: Identifiers (ASINs, UPCs, etc.)
            - includedData: Comma-delimited list of data sets to include
        """
        params = {
            'keywords': request.GET.get('keywords'),
            'marketplaceIds': request.GET.get('marketplaceIds'),
            'identifiers': request.GET.get('identifiers'),
            'includedData': request.GET.get('includedData'),
            'pageSize': request.GET.get('pageSize', 20),
        }
        
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.get('/catalog/2022-04-01/items', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))


class CatalogItemView(View):
    """Get a specific catalog item by ASIN"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, asin, *args, **kwargs):
        """Get catalog item details"""
        params = {
            'marketplaceIds': request.GET.get('marketplaceIds'),
            'includedData': request.GET.get('includedData'),
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.get(f'/catalog/2022-04-01/items/{asin}', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))

