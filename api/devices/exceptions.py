from rest_framework import serializers

class InvalidDataException(serializers.ValidationError):
    default_detail = "Invalid data provided."
    code = "invalid_data"

class DuplicateEntryException(serializers.ValidationError):
    default_detail = "Device with the same name already exists."
    code = "duplicate_entry"

class DeviceNotFoundException(serializers.ValidationError):
    default_detail = "Device with given id does not exist."
    code = "not_found"