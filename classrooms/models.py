from django.db import models


class Classroom(models.Model):
    class_id = models.CharField(max_length=20)
