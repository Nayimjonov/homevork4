from rest_framework import generics
from .models import Author
from books.models import Book
from .serializers import AuthorSerializer, AuthorBookSerializer
from .pagination import AuthorListPagination, AuthorBookListPagination


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorListPagination


class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = AuthorBookSerializer
    pagination_class = AuthorBookListPagination

    def get_queryset(self):
        return Book.objects.filter(authors__id=self.kwargs['pk'])
