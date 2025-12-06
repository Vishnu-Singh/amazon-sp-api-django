from django.urls import path
from .views import ReportsView, ReportView, ReportDocumentView

app_name = 'reports'

urlpatterns = [
    path('', ReportsView.as_view(), name='reports-list'),
    path('<str:report_id>/', ReportView.as_view(), name='report-detail'),
    path('documents/<str:document_id>/', ReportDocumentView.as_view(), name='report-document'),
]
