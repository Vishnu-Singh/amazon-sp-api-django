from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Merchant Fulfillment API helps you build applications for sellers.
"""

class BaseAPIView(View):
    """Base view for merchant_fulfillment API endpoints"""
    
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


class EligibleShipmentsView(BaseAPIView):
    """View for retrieving eligible shipping services"""
    
    def post(self, request, *args, **kwargs):
        """Handle POST request to get eligible shipping services"""
        endpoint = '/mfn/v0/eligibleShippingServices'
        return self.handle_request('POST', endpoint, request)
    
class ShipmentsView(BaseAPIView):
    """View for creating merchant fulfillment shipments"""
    
    def post(self, request, *args, **kwargs):
        """Handle POST request to create a shipment"""
        endpoint = '/mfn/v0/shipments'
        return self.handle_request('POST', endpoint, request)
    
