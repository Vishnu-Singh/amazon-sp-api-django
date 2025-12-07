from django.urls import path
from .views import SmallAndLightView

app_name = 'small_and_light'

urlpatterns = [
    path('enrollments/<str:seller_sku>/', SmallAndLightView.as_view(), name='small-and-light'),
]
