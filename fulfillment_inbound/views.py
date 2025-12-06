from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Fulfillment Inbound API helps you create and update inbound shipments.
"""

class BaseAPIView(View):
    """Base view for fulfillment_inbound API endpoints"""
    
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


class InboundShipmentsView(BaseAPIView):
    """View for shipments/"""
    
    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        endpoint = '/fulfillment_inbound/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        endpoint = '/fulfillment_inbound/...'  # TODO: Set correct endpoint
        return self.handle_request('POST', endpoint, request)
    
class InboundShipmentView(BaseAPIView):
    """View for shipments/<str:shipment_id>/"""
    
    def get(self, request, shipment_id, *args, **kwargs):
        """Handle GET request"""
        endpoint = f'/fulfillment_inbound/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
    def put(self, request, shipment_id, *args, **kwargs):
        """Handle PUT request"""
        endpoint = f'/fulfillment_inbound/...'  # TODO: Set correct endpoint
        return self.handle_request('PUT', endpoint, request)
    
