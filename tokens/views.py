from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Tokens API provides a secure way to access Personally Identifiable Information.
"""

class BaseAPIView(View):
    """Base view for tokens API endpoints"""
    
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


class RestrictedDataTokenView(BaseAPIView):
    """View for restrictedDataToken/"""
    
    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        endpoint = '/tokens/...'  # TODO: Set correct endpoint
        return self.handle_request('POST', endpoint, request)
    
