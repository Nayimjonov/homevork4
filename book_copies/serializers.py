from rest_framework import serializers
from .models import BookCopy
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn')

class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCopy
        fields = ('id', 'book', 'inventory_number', 'condition', 'is_available', 'added_date')


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['book'] = BookSerializer(instance.book).data
        return rep