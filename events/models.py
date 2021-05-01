from django.db import models
from books.models import BookList
from classrooms.models import Classroom


class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
