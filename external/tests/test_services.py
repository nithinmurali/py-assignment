from unittest.mock import Mock, patch
from django.test import TestCase
from common.responses import BadInputError, ServerError

from external.services.external import get_external_books, get_external_books_serialized


class ExternalBooksTestCase(TestCase):

    def setUp(self):
        self.mock_get_patcher = patch('external.services.external.requests.get')
        self.mock_get = self.mock_get_patcher.start()

    def tearDown(self):
        self.mock_get_patcher.stop()

    def test_get_books_when_response_is_ok(self):
        books = [{
            "url": "https://www.anapioficeandfire.com/api/books/1",
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "numberOfPages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "mediaType": "Hardcover",
            "released": "1996-08-01T00:00:00",
            "characters": [],
            "povCharacters": []
        }]

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json.return_value = books

        response = get_external_books("A Game of Thrones")

        self.assertListEqual(response, books)

    def test_get_books_when_response_is_not_ok(self):
        self.mock_get.return_value = Mock()
        self.mock_get.status_code = 500

        with self.assertRaises(ServerError):
            get_external_books("A Game of Thrones")


class ExternalBooksFormattedTestCase(TestCase):

    def setUp(self):
        self.mock_get_patcher = patch('external.services.external.get_external_books')
        self.mock_get = self.mock_get_patcher.start()

    def tearDown(self):
        self.mock_get_patcher.stop()

    def test_get_external_books_when_response_is_ok(self):
        books = [{
            "url": "https://www.anapioficeandfire.com/api/books/1",
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "numberOfPages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "mediaType": "Hardcover",
            "released": "1996-08-01T00:00:00",
            "characters": [],
            "povCharacters": []
        }]

        self.mock_get.return_value = books

        serializer = get_external_books_serialized("A Game of Thrones")
        response_book = serializer.validated_data[0]
        self.assertEqual(response_book["name"], "A Game of Thrones")
        self.assertEqual(response_book["number_of_pages"], 694)

    def test_get_external_books_when_response_is_bad(self):
        books = [{
            "url": "https://www.anapioficeandfire.com/api/books/1",
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "mediaType": "Hardcover",
            "released": "1996-08-01T00:00:00",
            "characters": [],
            "povCharacters": []
        }]

        self.mock_get.return_value = books

        with self.assertRaises(BadInputError):
            get_external_books_serialized("A Game of Thrones")
