from factory import DjangoModelFactory


class BookFactory(DjangoModelFactory):
    class Meta:
        model = "books.Book"
