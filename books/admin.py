from django.contrib import admin
from .models import Book, BookList


@admin.register(BookList, Book)
class BookAdmin(admin.ModelAdmin):
    pass

