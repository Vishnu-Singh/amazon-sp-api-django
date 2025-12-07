from django.urls import path
from .views import (
    DocumentationHomeView,
    SetupGuideView,
    APIDocumentationView,
    ChangelogView,
    APIReferenceJSONView,
)

app_name = 'documentation'

urlpatterns = [
    path('', DocumentationHomeView.as_view(), name='home'),
    path('setup/', SetupGuideView.as_view(), name='setup'),
    path('api/', APIDocumentationView.as_view(), name='api'),
    path('changelog/', ChangelogView.as_view(), name='changelog'),
    path('api/reference.json', APIReferenceJSONView.as_view(), name='api-reference-json'),
]
