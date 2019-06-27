from django.test import TestCase
from books.tests.factories import BookFactory
import books.services.core as book_services
from datetime import datetime
from books.models import Book
from rest_framework.exceptions import ValidationError
from common.responses import BadInputError


class TestBookCreate(TestCase):

    def test_new_book_create(self):
        book = book_services.create_book(name="test name", isbn='123-1234567890', authors=[], number_of_pages=10,
                                         publisher="test p", country="country", release_date=datetime.now().date())
        self.assertEqual(book.name, "test name")
        self.assertEqual(book.isbn, "123-1234567890")
        book.delete()

    def test_authors_not_list(self):
        with self.assertRaises(BadInputError):
            book = book_services.create_book(name="test name", isbn='123-1234567890', authors="", number_of_pages=10,
                                             publisher="test p", country="country", release_date=datetime.now().date())
            book.delete()

    def test_multiple_books_create(self):
        book1 = book_services.create_book(name="test name", isbn='123-1234567890', authors=["me"], number_of_pages=10,
                                          publisher="test p", country="country", release_date=datetime.now().date())
        book2 = book_services.create_book(name="test name", isbn='111-1234567890', authors=["me"], number_of_pages=10,
                                          publisher="test p", country="country", release_date=datetime.now().date())

        self.assertEqual(book1.name, book2.name)
        self.assertNotEqual(book1.id, book2.id)
        self.assertNotEqual(book1.isbn, book2.isbn)
        self.assertEqual(book1.authors, book2.authors)
        book1.delete()
        book2.delete()


class TestGetBook(TestCase):

    def setUp(self):
        self.book1 = BookFactory.create(name="test book1", isbn="111-1111111111")

    def tearDown(self):
        self.book1.delete()

    def test_get_book(self):
        book = book_services.get_a_book(self.book1.id)
        self.assertEqual(book.id, self.book1.id)
        self.assertEqual(book.name, self.book1.name)


class TestGetAllBook(TestCase):

    def setUp(self):
        self.num_books = 3
        self.books = []
        for i in range(self.num_books):
            self.books.append(BookFactory.create(name=f"test book{i}", isbn=f"111-111111111{i}"))

    def tearDown(self):
        for book in self.books:
            book.delete()

    def test_get_books(self):
        books = book_services.get_books()
        self.assertEqual(len(books), self.num_books)
        self.assertNotEqual(books[0].id, books[1].id)
        self.assertNotEqual(books[0].name, books[1].name)


class TestDeleteBook(TestCase):

    def test_delete_book(self):
        book = BookFactory.create()
        book_services.delete_book(book.id)

        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book.id)


class TestBookUpdate(TestCase):

    def setUp(self):
        self.book1 = BookFactory.create()

    def tearDown(self):
        self.book1.delete()

    def test_update_name(self):
        book_services.update_book(self.book1.id, name="new name")
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.name, "new name")

    def test_authors_update(self):
        book_services.update_book(self.book1.id, authors=['new author'])
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.authors, ['new author'])

    def test_book_dosent_exists(self):
        with self.assertRaises(BadInputError):
            book_services.update_book('cddae247-6902-4627-8066-df9a8e0f1b5c', name='new name')
