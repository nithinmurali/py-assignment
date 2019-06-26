from books.models import Book
from rest_framework.exceptions import ValidationError


def create_book(name, isbn, authors, number_of_pages, publisher, country, release_date):
    if type(authors) is not list:
        raise ValidationError("authors should be an array")
    book = Book.objects.create(name=name, isbn=isbn, authors=authors,number_of_pages=number_of_pages,
                               publisher=publisher, country=country, release_date=release_date)
    return book


def get_a_book(book_id):
    return Book.objects.get(id=book_id)


def get_books():
    return Book.objects.all()


def update_book(book_id, **kwargs):
    book = Book.objects.get(id=book_id)
    for k, v in kwargs.items():
        setattr(book, k, v)
    book.save()
    return book


def delete_book(book_id):
    Book.objects.get(id=book_id).delete()
    return
