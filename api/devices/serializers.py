# api/serializers.py

from rest_framework import serializers
from .models import Device

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
