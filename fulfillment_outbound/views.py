from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Fulfillment Outbound API helps you access fulfillment services.
"""

class BaseAPIView(View):
    """Base view for fulfillment_outbound API endpoints"""
    
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


class FulfillmentOrdersView(BaseAPIView):
    """View for resource collection"""
    
    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        endpoint = '/fba/outbound/2020-07-01/fulfillmentOrders'
        return self.handle_request('GET', endpoint, request)
    
    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        endpoint = '/fba/outbound/2020-07-01/fulfillmentOrders'
        return self.handle_request('POST', endpoint, request)
    
class FulfillmentOrderView(BaseAPIView):
    """View for resource collection"""
    
    def get(self, request, order_id, *args, **kwargs):
        """Handle GET request"""
        endpoint = f'/fba/outbound/2020-07-01/fulfillmentOrders/{order_id}'
        return self.handle_request('GET', endpoint, request)
    
    def put(self, request, order_id, *args, **kwargs):
        """Handle PUT request"""
        endpoint = f'/fba/outbound/2020-07-01/fulfillmentOrders/{order_id}'
        return self.handle_request('PUT', endpoint, request)
    
