from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core import exceptions as django_exceptions
from books.tests.factories import BookFactory
from books.serializers import BookSerializer
from books.models import Book
import books.views


class CreateBookTestCase(APITestCase):
    def setUp(self):
        self.create_url = reverse("books:books:books-list")
        self.book_model = BookFactory.build()
        self.book = None

    def test_create_success(self):
        data = BookSerializer(instance=self.book_model).data
        data.pop('id')
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['data']['book']['name'], self.book_model.name)


class GetBookTestCase(APITestCase):
    def setUp(self):
        self.book_model = BookFactory.create()
        self.get_url = reverse("books:books:books-detail", kwargs={'id': self.book_model.id})

    def test_get_book(self):
        response = self.client.get(self.get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data']['id'], str(self.book_model.id))
        self.assertEqual(response.json()['data']['name'], self.book_model.name)


class ListBooksTestCase(APITestCase):
    def setUp(self):
        self.get_url = reverse("books:books:books-list")
        BookFactory.create_batch(5)

    def test_list_books_(self):
        response = self.client.get(self.get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['data']), 5)


class DeleteBookTestCase(APITestCase):
    def setUp(self):
        self.book_model = BookFactory.create()
        self.get_url = reverse("books:books:books-detail", kwargs={'id': self.book_model.id})

    def test_delete_book(self):
        response = self.client.delete(self.get_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=self.book_model.id)


class UpdateBookTestCase(APITestCase):
    def setUp(self):
        self.book_model = BookFactory.create()
        self.get_url = reverse("books:books:books-detail", kwargs={'id': self.book_model.id})

    def test_update_book(self):
        data = {"name": "random test name"}
        response = self.client.patch(self.get_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = Book.objects.get(id=self.book_model.id)
        self.assertEquals(book.name, "random test name")

