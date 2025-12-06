from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Small and Light API helps you manage your Small and Light listings.
"""

class BaseAPIView(View):
    """Base view for small_and_light API endpoints"""
    
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


class SmallAndLightView(BaseAPIView):
    """View for resource collection"""
    
    def get(self, request, seller_sku, *args, **kwargs):
        """Handle GET request"""
        endpoint = f'/fba/smallAndLight/v1/enrollments/{seller_sku}'
        return self.handle_request('GET', endpoint, request)
    
    def put(self, request, seller_sku, *args, **kwargs):
        """Handle PUT request"""
        endpoint = f'/fba/smallAndLight/v1/enrollments/{seller_sku}'
        return self.handle_request('PUT', endpoint, request)
    
    def delete(self, request, seller_sku, *args, **kwargs):
        """Handle DELETE request"""
        endpoint = f'/fba/smallAndLight/v1/enrollments/{seller_sku}'
        return self.handle_request('DELETE', endpoint, request)
    
