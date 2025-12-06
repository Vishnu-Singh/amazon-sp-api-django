from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Notifications API enables you to subscribe to notifications.
"""

class BaseAPIView(View):
    """Base view for notifications API endpoints"""
    
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


class SubscriptionsView(BaseAPIView):
    """View for subscriptions/<str:notification_type>/"""
    
    def get(self, request, notification_type, *args, **kwargs):
        """Handle GET request"""
        endpoint = f'/notifications/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
    def post(self, request, notification_type, *args, **kwargs):
        """Handle POST request"""
        endpoint = f'/notifications/...'  # TODO: Set correct endpoint
        return self.handle_request('POST', endpoint, request)
    
    def delete(self, request, notification_type, *args, **kwargs):
        """Handle DELETE request"""
        endpoint = f'/notifications/...'  # TODO: Set correct endpoint
        return self.handle_request('DELETE', endpoint, request)
    
class DestinationsView(BaseAPIView):
    """View for destinations/"""
    
    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        endpoint = '/notifications/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        endpoint = '/notifications/...'  # TODO: Set correct endpoint
        return self.handle_request('POST', endpoint, request)
    
