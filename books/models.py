from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    publisher = models.CharField(max_length=50, null=True)
    lecture_name = models.CharField(max_length=50, null=True)
