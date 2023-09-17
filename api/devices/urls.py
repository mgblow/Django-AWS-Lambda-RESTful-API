from django.urls import path
from .views import DeviceCreateView

urlpatterns = [
    path('devices', DeviceCreateView.as_view(), name='device-create'),
]