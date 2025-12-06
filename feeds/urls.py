from django.urls import path
from .views import FeedsView, FeedView, FeedDocumentView

app_name = 'feeds'

urlpatterns = [
    path('', FeedsView.as_view(), name='feeds-list'),
    path('<str:feed_id>/', FeedView.as_view(), name='feed-detail'),
    path('documents/', FeedDocumentView.as_view(), name='feed-document-create'),
    path('documents/<str:document_id>/', FeedDocumentView.as_view(), name='feed-document-detail'),
]
