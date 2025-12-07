from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.conf import settings
import json

# Create your views here.

class DocumentationHomeView(View):
    """
    Main documentation home page with project overview
    """
    
    def get(self, request):
        """Display documentation home page"""
        return render(request, 'documentation/home.html', {
            'project_name': 'Amazon SP-API Django Integration',
            'version': '1.0.0',
            'description': 'Complete Django project for Amazon Selling Partner API integration',
        })


class SetupGuideView(View):
    """
    Setup and installation guide
    """
    
    def get(self, request):
        """Display setup guide"""
        return render(request, 'documentation/setup.html')


class APIDocumentationView(View):
    """
    Interactive API documentation with all endpoints
    """
    
    def get(self, request):
        """Display API documentation"""
        
        # Define all API categories with their endpoints
        api_categories = {
            'feeds': {
                'name': 'Feeds API',
                'description': 'Upload data to Amazon and track processing status',
                'base_path': '/api/feeds/',
                'version': '2021-06-30',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/feeds/',
                        'sp_api_path': '/feeds/2021-06-30/feeds',
                        'description': 'Get list of feeds',
                        'parameters': [
                            {'name': 'feedTypes', 'required': False, 'description': 'A list of feed types'},
                            {'name': 'marketplaceIds', 'required': True, 'description': 'Marketplace identifiers'},
                            {'name': 'pageSize', 'required': False, 'description': 'Number of feeds to return (default: 10)'},
                            {'name': 'processingStatuses', 'required': False, 'description': 'List of processing statuses'},
                        ]
                    },
                    {
                        'method': 'POST',
                        'path': '/api/feeds/',
                        'sp_api_path': '/feeds/2021-06-30/feeds',
                        'description': 'Create a new feed',
                        'parameters': []
                    },
                    {
                        'method': 'GET',
                        'path': '/api/feeds/{feed_id}/',
                        'sp_api_path': '/feeds/2021-06-30/feeds/{feedId}',
                        'description': 'Get information about a specific feed',
                        'parameters': []
                    },
                ]
            },
            'catalog': {
                'name': 'Catalog Items API',
                'description': 'Search and retrieve Amazon catalog information',
                'base_path': '/api/catalog/',
                'version': '2022-04-01',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/catalog/',
                        'sp_api_path': '/catalog/2022-04-01/items',
                        'description': 'Search for catalog items',
                        'parameters': [
                            {'name': 'keywords', 'required': False, 'description': 'Keywords to search for'},
                            {'name': 'marketplaceIds', 'required': True, 'description': 'Marketplace identifiers'},
                            {'name': 'identifiers', 'required': False, 'description': 'Product identifiers (ASINs, UPCs)'},
                        ]
                    },
                    {
                        'method': 'GET',
                        'path': '/api/catalog/{asin}/',
                        'sp_api_path': '/catalog/2022-04-01/items/{asin}',
                        'description': 'Get catalog item by ASIN',
                        'parameters': [
                            {'name': 'marketplaceIds', 'required': True, 'description': 'Marketplace identifiers'},
                        ]
                    },
                ]
            },
            'orders': {
                'name': 'Orders API',
                'description': 'Retrieve and manage order information',
                'base_path': '/api/orders/',
                'version': 'v0',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/orders/',
                        'sp_api_path': '/orders/v0/orders',
                        'description': 'Get list of orders',
                        'parameters': [
                            {'name': 'marketplaceIds', 'required': True, 'description': 'Marketplace identifiers'},
                            {'name': 'createdAfter', 'required': False, 'description': 'Orders created after (ISO 8601)'},
                            {'name': 'orderStatuses', 'required': False, 'description': 'List of order statuses'},
                        ]
                    },
                    {
                        'method': 'GET',
                        'path': '/api/orders/{order_id}/',
                        'sp_api_path': '/orders/v0/orders/{orderId}',
                        'description': 'Get specific order details',
                        'parameters': []
                    },
                ]
            },
            'listings': {
                'name': 'Listings Items API',
                'description': 'Create, read, update, and delete product listings',
                'base_path': '/api/listings/',
                'version': '2021-08-01',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/listings/{seller_id}/{sku}/',
                        'sp_api_path': '/listings/2021-08-01/items/{sellerId}/{sku}',
                        'description': 'Get listing item',
                        'parameters': [
                            {'name': 'marketplaceIds', 'required': True, 'description': 'Marketplace identifiers'},
                        ]
                    },
                    {
                        'method': 'PUT',
                        'path': '/api/listings/{seller_id}/{sku}/',
                        'sp_api_path': '/listings/2021-08-01/items/{sellerId}/{sku}',
                        'description': 'Create or update listing',
                        'parameters': []
                    },
                    {
                        'method': 'DELETE',
                        'path': '/api/listings/{seller_id}/{sku}/',
                        'sp_api_path': '/listings/2021-08-01/items/{sellerId}/{sku}',
                        'description': 'Delete listing',
                        'parameters': []
                    },
                ]
            },
            'reports': {
                'name': 'Reports API',
                'description': 'Generate and retrieve various seller reports',
                'base_path': '/api/reports/',
                'version': '2021-06-30',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/reports/',
                        'sp_api_path': '/reports/2021-06-30/reports',
                        'description': 'Get list of reports',
                        'parameters': []
                    },
                    {
                        'method': 'POST',
                        'path': '/api/reports/',
                        'sp_api_path': '/reports/2021-06-30/reports',
                        'description': 'Create a report',
                        'parameters': []
                    },
                ]
            },
            'fulfillment_inbound': {
                'name': 'FBA Inbound API',
                'description': 'Manage inbound shipments to Amazon FBA',
                'base_path': '/api/fulfillment-inbound/',
                'version': 'v0',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/fulfillment-inbound/shipments/',
                        'sp_api_path': '/fba/inbound/v0/shipments',
                        'description': 'Get inbound shipments',
                        'parameters': []
                    },
                    {
                        'method': 'POST',
                        'path': '/api/fulfillment-inbound/shipments/',
                        'sp_api_path': '/fba/inbound/v0/shipments',
                        'description': 'Create inbound shipment',
                        'parameters': []
                    },
                ]
            },
            'fulfillment_outbound': {
                'name': 'FBA Outbound API',
                'description': 'Access Multi-Channel Fulfillment services',
                'base_path': '/api/fulfillment-outbound/',
                'version': '2020-07-01',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/fulfillment-outbound/orders/',
                        'sp_api_path': '/fba/outbound/2020-07-01/fulfillmentOrders',
                        'description': 'Get fulfillment orders',
                        'parameters': []
                    },
                ]
            },
            'merchant_fulfillment': {
                'name': 'Merchant Fulfillment API',
                'description': 'Purchase shipping for seller-fulfilled orders',
                'base_path': '/api/merchant-fulfillment/',
                'version': 'v0',
                'endpoints': [
                    {
                        'method': 'POST',
                        'path': '/api/merchant-fulfillment/eligibleShippingServices/',
                        'sp_api_path': '/mfn/v0/eligibleShippingServices',
                        'description': 'Get eligible shipping services',
                        'parameters': []
                    },
                ]
            },
            'finance': {
                'name': 'Finances API',
                'description': 'Retrieve financial information and transactions',
                'base_path': '/api/finance/',
                'version': 'v0',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/finance/financialEvents/',
                        'sp_api_path': '/finances/v0/financialEvents',
                        'description': 'Get financial events',
                        'parameters': []
                    },
                ]
            },
            'product_pricing': {
                'name': 'Product Pricing API',
                'description': 'Get pricing information for products',
                'base_path': '/api/product-pricing/',
                'version': 'v0',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/product-pricing/pricing/',
                        'sp_api_path': '/products/pricing/v0/price',
                        'description': 'Get product pricing',
                        'parameters': []
                    },
                ]
            },
            'product_fees': {
                'name': 'Product Fees API',
                'description': 'Estimate Amazon fees for products',
                'base_path': '/api/product-fees/',
                'version': 'v0',
                'endpoints': [
                    {
                        'method': 'POST',
                        'path': '/api/product-fees/feesEstimate/',
                        'sp_api_path': '/products/fees/v0/feesEstimate',
                        'description': 'Get fee estimates',
                        'parameters': []
                    },
                ]
            },
            'sellers': {
                'name': 'Sellers API',
                'description': 'Get seller account information',
                'base_path': '/api/sellers/',
                'version': 'v1',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/sellers/marketplaceParticipations/',
                        'sp_api_path': '/sellers/v1/marketplaceParticipations',
                        'description': 'Get marketplace participations',
                        'parameters': []
                    },
                ]
            },
            'inventory': {
                'name': 'FBA Inventory API',
                'description': 'Retrieve FBA inventory data',
                'base_path': '/api/inventory/',
                'version': 'v1',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/inventory/summaries/',
                        'sp_api_path': '/fba/inventory/v1/summaries',
                        'description': 'Get inventory summaries',
                        'parameters': []
                    },
                ]
            },
            'shipping': {
                'name': 'Shipping API',
                'description': 'Access Amazon shipping services',
                'base_path': '/api/shipping/',
                'version': 'v1',
                'endpoints': [
                    {
                        'method': 'POST',
                        'path': '/api/shipping/shipments/',
                        'sp_api_path': '/shipping/v1/shipments',
                        'description': 'Create shipment',
                        'parameters': []
                    },
                ]
            },
            'notifications': {
                'name': 'Notifications API',
                'description': 'Subscribe to and manage SP-API notifications',
                'base_path': '/api/notifications/',
                'version': 'v1',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/notifications/subscriptions/{notification_type}/',
                        'sp_api_path': '/notifications/v1/subscriptions/{notificationType}',
                        'description': 'Get subscription',
                        'parameters': []
                    },
                ]
            },
            'authorization': {
                'name': 'Authorization API',
                'description': 'Manage authorization and permissions',
                'base_path': '/api/authorization/',
                'version': 'v1',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/authorization/authorizationCode/',
                        'sp_api_path': '/authorization/v1/authorizationCode',
                        'description': 'Get authorization code',
                        'parameters': []
                    },
                ]
            },
            'small_and_light': {
                'name': 'Small and Light API',
                'description': 'Manage Small and Light program enrollments',
                'base_path': '/api/small-and-light/',
                'version': 'v1',
                'endpoints': [
                    {
                        'method': 'GET',
                        'path': '/api/small-and-light/enrollments/{seller_sku}/',
                        'sp_api_path': '/fba/smallAndLight/v1/enrollments/{sellerSKU}',
                        'description': 'Get enrollment status',
                        'parameters': []
                    },
                ]
            },
            'tokens': {
                'name': 'Tokens API',
                'description': 'Generate restricted data tokens for PII access',
                'base_path': '/api/tokens/',
                'version': '2021-03-01',
                'endpoints': [
                    {
                        'method': 'POST',
                        'path': '/api/tokens/restrictedDataToken/',
                        'sp_api_path': '/tokens/2021-03-01/restrictedDataToken',
                        'description': 'Create restricted data token',
                        'parameters': []
                    },
                ]
            },
        }
        
        return render(request, 'documentation/api.html', {
            'api_categories': api_categories,
        })


class ChangelogView(View):
    """
    Display changelog and version history
    """
    
    def get(self, request):
        """Display changelog"""
        return render(request, 'documentation/changelog.html')


class APIReferenceJSONView(View):
    """
    Return API documentation as JSON (OpenAPI-style format)
    """
    
    def get(self, request):
        """Return API documentation in JSON format"""
        
        api_spec = {
            'openapi': '3.0.0',
            'info': {
                'title': 'Amazon SP-API Django Integration',
                'version': '1.0.0',
                'description': 'RESTful API proxy for Amazon Selling Partner API',
                'contact': {
                    'name': 'API Support',
                    'url': 'https://github.com/Vishnu-Singh/amazon-sp-api-django'
                }
            },
            'servers': [
                {
                    'url': 'http://localhost:8000',
                    'description': 'Development server'
                }
            ],
            'paths': {
                '/api/feeds/': {
                    'get': {
                        'summary': 'Get list of feeds',
                        'tags': ['Feeds'],
                        'parameters': [
                            {
                                'name': 'marketplaceIds',
                                'in': 'query',
                                'required': True,
                                'schema': {'type': 'string'}
                            }
                        ]
                    },
                    'post': {
                        'summary': 'Create a new feed',
                        'tags': ['Feeds']
                    }
                },
                '/api/orders/': {
                    'get': {
                        'summary': 'Get list of orders',
                        'tags': ['Orders'],
                        'parameters': [
                            {
                                'name': 'marketplaceIds',
                                'in': 'query',
                                'required': True,
                                'schema': {'type': 'string'}
                            }
                        ]
                    }
                },
                '/api/catalog/': {
                    'get': {
                        'summary': 'Search catalog items',
                        'tags': ['Catalog']
                    }
                }
            },
            'components': {
                'securitySchemes': {
                    'AmazonSPAPI': {
                        'type': 'oauth2',
                        'flows': {
                            'authorizationCode': {
                                'authorizationUrl': 'https://api.amazon.com/auth/o2/authorize',
                                'tokenUrl': 'https://api.amazon.com/auth/o2/token',
                                'scopes': {}
                            }
                        }
                    }
                }
            }
        }
        
        return JsonResponse(api_spec, json_dumps_params={'indent': 2})
