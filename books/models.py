from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    name = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=14)
    authors = ArrayField(models.CharField(max_length=1000))
    number_of_pages = models.PositiveIntegerField()
    publisher = models.CharField(max_length=1000)
    country = models.CharField(max_length=500)
    release_date = models.DateField()
