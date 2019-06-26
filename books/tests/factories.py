from factory import DjangoModelFactory


class BookFactory(DjangoModelFactory):
    class Meta:
        model = "books.Book"

    name = "test book"
    isbn = "123-1234567890"
    authors = []
