from django.urls import path
from .views import FinancialEventsView, FinancialEventGroupsView

app_name = 'finance'

urlpatterns = [
    path('financialEvents/', FinancialEventsView.as_view(), name='financial-events'),
    path('financialEventGroups/', FinancialEventGroupsView.as_view(), name='financial-event-groups'),
]
