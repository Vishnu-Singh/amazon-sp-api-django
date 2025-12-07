from django.urls import path
from .views import RestrictedDataTokenView

app_name = 'tokens'

urlpatterns = [
    path('restrictedDataToken/', RestrictedDataTokenView.as_view(), name='rdt'),
]
