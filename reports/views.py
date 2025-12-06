from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

"""
The Reports API lets you retrieve reports about your selling account.
"""

class BaseAPIView(View):
    """Base view for reports API endpoints"""
    
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


class ReportsView(BaseAPIView):
    """View for """
    
    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        endpoint = '/reports/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        endpoint = '/reports/...'  # TODO: Set correct endpoint
        return self.handle_request('POST', endpoint, request)
    
class ReportView(BaseAPIView):
    """View for <str:report_id>/"""
    
    def get(self, request, report_id, *args, **kwargs):
        """Handle GET request"""
        endpoint = f'/reports/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
class ReportDocumentView(BaseAPIView):
    """View for documents/<str:document_id>/"""
    
    def get(self, request, document_id, *args, **kwargs):
        """Handle GET request"""
        endpoint = f'/reports/...'  # TODO: Set correct endpoint
        return self.handle_request('GET', endpoint, request)
    
