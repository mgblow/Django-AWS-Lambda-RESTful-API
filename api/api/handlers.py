# handlers.py

from django.http import JsonResponse

def custom_500_error_handler(request, *args, **kwargs):
    response_data = {
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred on the server.',
    }
    return JsonResponse(response_data, status=500)
