import requests
from external.serializers import ExternalBookSerializer
from common.responses import BadInputError, ServerError
from rest_framework.exceptions import ValidationError
from django.conf import settings


def get_external_books(name):
    response = requests.get(settings.FIRE_AND_ICE_URL, params={'name': name})
    if response.status_code == 200:
        return response.json()
    else:
        raise ServerError("Error in API call")


def get_external_books_serialized(name):
    response = get_external_books(name)
    serializer = ExternalBookSerializer(data=response, many=True)
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        raise BadInputError(e.detail)
    return serializer
