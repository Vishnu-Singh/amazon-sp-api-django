from django.urls import path
from .views import AuthorizationView

app_name = 'authorization'

urlpatterns = [
    path('authorizationCode/', AuthorizationView.as_view(), name='authorization'),
]
