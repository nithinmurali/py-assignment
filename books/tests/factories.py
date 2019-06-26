from factory import DjangoModelFactory


class BookFactory(DjangoModelFactory):
    class Meta:
        model = "books.Book"

    name = "test book"
    isbn = "123-1234567890"
    authors = []
    number_of_pages = 1
    publisher = "some publisher"
    country = "country"
    release_date = "2018-01-01"
