from django.db import models
from books.models import Book

class BookCopy(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_copies')
    inventory_number = models.CharField(max_length=50, unique=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=CONDITION_CHOICES[0][0])
    is_available = models.BooleanField()
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Book Copy'
        verbose_name_plural = 'Book Copies'

    def __str__(self):
        return self.book.title

