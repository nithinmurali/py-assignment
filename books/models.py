from django.db import models
from django.contrib.postgres.fields import ArrayField
from uuid import uuid4


class Book(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=26)
    authors = ArrayField(models.CharField(max_length=1000))
    number_of_pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=1000)
    country = models.CharField(max_length=500)
    release_date = models.DateField()
