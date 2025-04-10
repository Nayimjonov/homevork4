from rest_framework import serializers
from .models import Book
from authors.models import Author
from genres.models import Genre


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    copies_available = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'genre',
            'isbn',
            'published_date',
            'description',
            'page_count',
            'language',
            'copies_available'
        )

    def get_copies_available(self, obj):
        return obj.book_copies.filter(is_available=True).count()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['authors'] = BookAuthorSerializer(instance.authors, many=True).data
        rep['genre'] = BookGenreSerializer(instance.genre).data
        return rep