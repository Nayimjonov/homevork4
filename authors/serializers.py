from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality', 'books_count')

    def get_books_count(self, instance):
        return instance.books.count()

class AuthorBookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    isbn = serializers.CharField()
    published_date = serializers.DateField()
    copies_available = serializers.SerializerMethodField()

    def get_copies_available(self, obj):
        return obj.book_copies.filter(is_available=True).count()

