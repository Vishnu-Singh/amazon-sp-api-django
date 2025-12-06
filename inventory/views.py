from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The FBA Inventory API helps you programmatically retrieve FBA inventory data.
"""

class BaseAPIView(View):
    """Base view for inventory API endpoints"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def handle_request(self, method, endpoint, request):
        """Handle API request"""
        params = dict(request.GET.items())
        data = None
        
        if method in ['POST', 'PUT', 'PATCH']:
            try:
                data = json.loads(request.body) if request.body else {}
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        response = self.client.make_request(method, endpoint, params=params, data=data)
        return JsonResponse(response, status=response.get('status_code', 200))


class InventorySummariesView(BaseAPIView):
    """View for summaries/"""
    
    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        endpoint = '/inventory/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
