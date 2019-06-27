import requests
from urllib.parse import quote
from common.responses import BadInputError, ServerError


def get_external_books(name):
    response = requests.get('https://www.anapioficeandfire.com/api/books', params={'q': quote(name)})
    if response.status_code == 200:
        return response.json()
    else:
        raise ServerError("Error in API call")
