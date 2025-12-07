from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from amazon_sp_api.utils.sp_api_client import AmazonSPAPIClient
import json

# Create your views here.

class FeedsView(View):
    """
    Proxy view for Amazon SP-API Feeds endpoints
    
    The Feeds API lets you upload data to Amazon and get information about the processing of those uploads.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, *args, **kwargs):
        """
        Get feeds
        
        Query Parameters:
            - feedTypes: A list of feed types
            - marketplaceIds: A list of marketplace identifiers
            - pageSize: The maximum number of feeds to return
            - processingStatuses: A list of processing statuses
        """
        params = {
            'feedTypes': request.GET.get('feedTypes'),
            'marketplaceIds': request.GET.get('marketplaceIds'),
            'pageSize': request.GET.get('pageSize', 10),
            'processingStatuses': request.GET.get('processingStatuses'),
        }
        
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self.client.get('/feeds/2021-06-30/feeds', params=params)
        return JsonResponse(response, status=response.get('status_code', 200))
    
    def post(self, request, *args, **kwargs):
        """
        Create a feed
        
        Body Parameters:
            - feedType: The feed type
            - marketplaceIds: A list of marketplace identifiers
            - inputFeedDocumentId: The document identifier returned by createFeedDocument
        """
        try:
            data = json.loads(request.body) if request.body else {}
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        response = self.client.post('/feeds/2021-06-30/feeds', data=data)
        return JsonResponse(response, status=response.get('status_code', 200))


class FeedView(View):
    """Get a specific feed by ID"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, feed_id, *args, **kwargs):
        """Get information about a feed"""
        response = self.client.get(f'/feeds/2021-06-30/feeds/{feed_id}')
        return JsonResponse(response, status=response.get('status_code', 200))
    
    def delete(self, request, feed_id, *args, **kwargs):
        """Cancel a feed"""
        response = self.client.delete(f'/feeds/2021-06-30/feeds/{feed_id}')
        return JsonResponse(response, status=response.get('status_code', 200))


class FeedDocumentView(View):
    """Create and get feed documents"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = AmazonSPAPIClient()
    
    def get(self, request, document_id, *args, **kwargs):
        """Get feed document information"""
        response = self.client.get(f'/feeds/2021-06-30/documents/{document_id}')
        return JsonResponse(response, status=response.get('status_code', 200))
    
    def post(self, request, *args, **kwargs):
        """Create a feed document"""
        try:
            data = json.loads(request.body) if request.body else {}
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        response = self.client.post('/feeds/2021-06-30/documents', data=data)
        return JsonResponse(response, status=response.get('status_code', 200))

