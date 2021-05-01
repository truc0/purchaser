from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    publisher = models.CharField(max_length=50, null=True)
    lecture_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name} (${self.price})"


class BookList(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
