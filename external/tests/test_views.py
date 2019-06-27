from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class GetExternalBookTestCase(APITestCase):

    def setUp(self):
        self.get_url = reverse("external:get-external-books")
        self.book_name_encoded = 'A%20Game%20of%20Thrones'
        self.book = {
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
            "release_date": "1996-08-01",
        }

    def test_get_book(self):
        response = self.client.get(self.get_url + "?name=" + self.book_name_encoded, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['data'][0]['isbn'], str(self.book['isbn']))
        self.assertEqual(response.json()['data'][0]['name'], self.book['name'])
