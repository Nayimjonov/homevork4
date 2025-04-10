from django.db import models
from authors.models import Author
from genres.models import Genre


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=100, unique=True)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title
