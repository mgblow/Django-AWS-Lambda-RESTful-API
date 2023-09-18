from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from devices.models import Device  
from devices.views import DeviceCreateView

class DeviceCreateViewTestCase(TestCase):
    def setUp(self):
        # Create a test device data
        self.device_data = {
            "id": "id01",
            "deviceModel": "/devicemodels/id01",
            "name": "Sensor",
            "note": "Testing a sensor.",
            "serial": "A020000102"
        }

    def test_device_creation(self):
        # Get the initial count of devices in the database
        initial_device_count = Device.objects.count()

        # Use reverse to generate the URL for the DeviceCreateView
        url = reverse("device-create")

        # Send a POST request to create a new device
        response = self.client.post(url, data=self.device_data, content_type="application/json")

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if a new device was added to the database
        self.assertEqual(Device.objects.count(), initial_device_count + 1)

        # Check if the response data matches the expected JSON response
        expected_response_data = {
            "id": "id01",
            "deviceModel": "/devicemodels/id01",
            "name": "Sensor",
            "note": "Testing a sensor.",
            "serial": "A020000102"
        }
        self.assertJSONEqual(str(response.content, encoding="utf8"), expected_response_data)

    def test_invalid_device_creation(self):
        # Remove a required field from the device data to make it invalid
        invalid_device_data = self.device_data.copy()
        del invalid_device_data["name"]

        # Get the initial count of devices in the database
        initial_device_count = Device.objects.count()

        # Use reverse to generate the URL for the DeviceCreateView
        url = reverse("device-create")

        # Send a POST request with invalid data
        response = self.client.post(url, data=invalid_device_data, content_type="application/json")

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if no new device was added to the database
        self.assertEqual(Device.objects.count(), initial_device_count)
