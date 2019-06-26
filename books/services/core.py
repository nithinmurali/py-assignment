from books.models import Book
from rest_framework.exceptions import ValidationError
from common.responses import BadInputError


def create_book(name, isbn, authors, number_of_pages, publisher, country, release_date):
    if type(authors) is not list:
        raise BadInputError(f"authors should be an array not {authors}")
    # TODO check date
    book = Book.objects.create(name=name, isbn=isbn, authors=authors,number_of_pages=number_of_pages,
                               publisher=publisher, country=country, release_date=release_date)
    return book


def get_a_book(book_id):
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise BadInputError(f"The book with id {book_id} doesnt exist")


def get_books():
    return Book.objects.all()


def update_book(book_id, **kwargs):
    book = get_a_book(book_id)
    for k, v in kwargs.items():
        setattr(book, k, v)
    book.save()
    return book


def delete_book(book_id):
    book = get_a_book(book_id)
    book.delete()
