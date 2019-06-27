from django.urls import path
from external import views

app_name = 'external'

urlpatterns = [
    path('external-books', views.api_get_external_books, name='get-external-books'),
]
