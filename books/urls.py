from django.urls import path, include
from rest_framework import routers
from books.views import BookViewSet

app_name = 'books'

router = routers.SimpleRouter()
router.register('books', BookViewSet, 'books')

urlpatterns = [
    path('', include((router.urls, app_name))),
]
