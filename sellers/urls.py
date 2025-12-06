from django.urls import path
from .views import MarketplaceParticipationsView

app_name = 'sellers'

urlpatterns = [
    path('marketplaceParticipations/', MarketplaceParticipationsView.as_view(), name='marketplace-participations'),
]
