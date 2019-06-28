import requests
from urllib.parse import quote
from external.serializers import ExternalBookSerializer
from common.responses import BadInputError, ServerError
from django.conf import settings


def get_external_books(name):
    response = requests.get(settings.FIRE_AND_ICE_URL, params={'name': quote(name)})
    if response.status_code == 200:
        return response.json()
    else:
        raise ServerError("Error in API call")


def get_external_books_serialized(name):
    response = get_external_books(name)
    serializer = ExternalBookSerializer(data=response, many=True)
    serializer.is_valid(raise_exception=True)
    return serializer
