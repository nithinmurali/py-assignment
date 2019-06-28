from books.models import Book
from common.responses import BadInputError


def create_book(name, isbn, authors, number_of_pages, publisher, country, release_date):
    """
    create a book given its properties

    :param name: name of book
    :param isbn: isbn
    :param authors: list of authors
    :param number_of_pages: number_of_pages
    :param publisher: publisher name
    :param country: country name
    :param release_date: release date
    :return: created Book object
    """
    if type(authors) is not list:
        raise BadInputError(f"authors should be an array not {authors}")
    book = Book.objects.create(name=name, isbn=isbn, authors=authors, number_of_pages=number_of_pages,
                               publisher=publisher, country=country, release_date=release_date)
    return book


def get_a_book(book_id):
    """
    get a book given id

    :param book_id: id of book to retrieve
    :return: book object
    """
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise BadInputError(f"The book with id {book_id} doesnt exist")


def get_books():
    """
    get all books
    :return: list of book objects
    """
    return Book.objects.all()


def update_book(book_id, **kwargs):
    """
    update book given its id with given attributes

    :param book_id: id of book to update
    :param kwargs: book attributes to update
    :return: updated book object
    """
    book = get_a_book(book_id)
    for k, v in kwargs.items():
        setattr(book, k, v)
    book.save()
    return book


def delete_book(book_id):
    """
    delete a book given id

    :param book_id: id of book to delete
    """
    book = get_a_book(book_id)
    book.delete()
