from django.urls import path, re_path
from .views import DeviceCreateView, DeviceDetailView

urlpatterns = [
    path('devices', DeviceCreateView.as_view(), name='device-create'),
    path('devices/<str:device_id>/', DeviceDetailView.as_view(), name='device-detail'),
]
