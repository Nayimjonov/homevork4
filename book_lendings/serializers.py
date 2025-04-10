from rest_framework import serializers
from .models import BookLending, BookCopy


class BookLendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLending
        fields = (
            'id',
            'book_copy',
            'borrower_name',
            'borrower_email',
            'borrowed_date',
            'due_date',
            'returned_date',
            'status',
        )


class BookLendingListSerializer(BookLendingSerializer):
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        book_copy = instance.book_copy
        rep['book_copy'] = {
            'id': book_copy.id,
            'inventory_number': book_copy.inventory_number,
            'book': {
                'id': book_copy.book.id,
                'title': book_copy.book.title,
                'isbn': book_copy.book.isbn
            }
        }
        return rep
