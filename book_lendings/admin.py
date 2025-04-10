from django.contrib import admin
from .models import BookLending


@admin.register(BookLending)
class BookLendingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book_copy',
        'borrower_name',
        'borrowed_date',
        'due_date',
        'returned_date',
        'status'
    )
    search_fields = ('borrower_name', 'borrower_email')
    list_filter = ('status', 'book_copy', 'borrowed_date')