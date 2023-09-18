from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device
from .serializers import DeviceSerializer
# Import custom exceptions
from .exceptions import InvalidDataException, DuplicateEntryException, DeviceNotFoundException  

class DeviceCreateView(APIView):
    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)  # Raise custom exceptions
        except InvalidDataException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except DuplicateEntryException as e:
            return Response({"error": str(e)}, status=status.HTTP_409_CONFLICT)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeviceDetailView(APIView):
    def get(self, request, device_id, format=None):
        try:
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            raise DeviceNotFoundException("Device not found")

        serializer = DeviceSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)