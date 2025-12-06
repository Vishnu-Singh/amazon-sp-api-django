from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Sellers API helps you retrieve information about your seller account.
"""

class BaseAPIView(View):
    """Base view for sellers API endpoints"""
    
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


class MarketplaceParticipationsView(BaseAPIView):
    """View for resource collection"""
    
    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        endpoint = '/sellers/v1/marketplaceParticipations'
        return self.handle_request('GET', endpoint, request)
    
