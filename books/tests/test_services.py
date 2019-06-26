from django.test import TestCase
from books.tests.factories import BookFactory
import books.services.core as book_services
from datetime import datetime
from rest_framework.exceptions import ValidationError


class TestBookCreate(TestCase):

    def test_new_book_create(self):
        book = book_services.create_book(name="test name", isbn='123-1234567890', authors=[], number_of_pages=10,
                                         publisher="test p", country="country", release_date=datetime.now().date())
        self.assertEqual(book.name, "test name")
        self.assertEqual(book.isbn, "123-1234567890")
        book.delete()

    def test_authors_not_list(self):
        with self.assertRaises(ValidationError):  # TODO change
            book = book_services.create_book(name="test name", isbn='123-1234567890', authors="", number_of_pages=10,
                                             publisher="test p", country="country", release_date=datetime.now().date())
            book.delete()


class TestBookUpdate(TestCase):

    def setUp(self):
        self.book1 = BookFactory.create(name="test book1", isbn="111-1111111111")

    def tearDown(self):
        self.book1.delete()
