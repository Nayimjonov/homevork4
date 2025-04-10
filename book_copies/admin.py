from django.contrib import admin
from .models import BookCopy


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'book', 'inventory_number', 'condition',
        'is_available', 'added_date',
    )
    list_filter = ('condition', 'book', 'is_available', 'added_date')
