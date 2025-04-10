from django.utils import timezone
from rest_framework import serializers
from .models import BookLending

class BookLendingSerializer(serializers.ModelSerializer):
    days_remaining = serializers.SerializerMethodField()

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
            'days_remaining',
        )

    def get_days_remaining(self, obj):
        due_date = obj.due_date
        if due_date:
            remaining_days = (due_date - timezone.now()).days
            return remaining_days
        return None

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        book_copy = instance.book_copy
        rep['book_copy'] = {
            'id': book_copy.id,
            'book': {
                'id': book_copy.book.id,
                'title': book_copy.book.title,
                'isbn': book_copy.book.isbn,
                'authors': [{'id': author.id, 'first_name': author.first_name, 'last_name': author.last_name} for author in book_copy.book.authors.all()]
            },
            'inventory_number': book_copy.inventory_number,
            'condition': book_copy.condition,
        }
        return rep
