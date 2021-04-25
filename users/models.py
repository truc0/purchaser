from django.contrib.auth.models import AbstractUser
from django.db import models

from classrooms.models import Classroom


class User(AbstractUser):
    pass


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
