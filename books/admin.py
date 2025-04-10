from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'genre', 'isbn',
        'published_date', 'page_count', 'language'
    )
    search_fields = ('title', 'description', 'isbn',)
    list_filter = ('genre', 'language', 'published_date')
