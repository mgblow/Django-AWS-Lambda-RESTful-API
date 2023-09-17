# api/models.py
# This model defines the interface for devices

from django.db import models

class Device(models.Model):
    id = models.CharField(max_length=255, unique=True)
    deviceModel = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    note = models.TextField()
    serial = models.CharField(max_length=20)

    def __str__(self):
        return self.name
