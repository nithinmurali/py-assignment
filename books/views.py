from rest_framework import viewsets
import books.services.core as book_services
from books.serializers import BookSerializer
from common.responses import data_response


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return book_services.get_books()

    def get_object(self):
        return book_services.get_a_book(book_id=self.kwargs['id'])

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return data_response(200, serializer.data)

    def list(self, request, *args, **kwargs):
        objects = self.get_queryset()
        serializer = BookSerializer(objects, many=True)
        return data_response(200, serializer.data)

    def destroy(self, request, *args, **kwargs):
        book = book_services.get_a_book(book_id=kwargs['id'])
        book_services.delete_book(book_id=kwargs['id'])
        return data_response(204, [], "success", f"The book {book.name} was deleted successfully")

    def update(self, request, *args, **kwargs):
        book = book_services.update_book(self.kwargs['id'], **request.data)
        serializer = self.get_serializer(instance=book)
        return data_response(200, serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        book = book_services.create_book(**serializer.validated_data)
        serializer = self.get_serializer(instance=book)
        return data_response(201, {"book": serializer.data})
