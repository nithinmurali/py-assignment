from external.services.external import get_external_books_serialized
from common.responses import data_response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_get_external_books(request, format=None):
    book_name = request.query_params.get('book', '')
    books = get_external_books_serialized(book_name)
    return data_response(200, data=books.data)
