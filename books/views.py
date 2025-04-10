from rest_framework import generics
from .models import Book
from book_copies.models import BookCopy
from .serializers import BookSerializer, BookCopySerializer
from .pagination import BookPagination, BookCopyPagination


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCopyListView(generics.ListAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    pagination_class = BookCopyPagination

    def get_queryset(self):
        book_id = self.kwargs['pk']
        return BookCopy.objects.filter(book__id=book_id)