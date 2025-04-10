from rest_framework import generics
from .models import BookCopy
from .serializers import BookCopySerializer
from .pagination import BookCopyPagination


class BookCopyListCreateView(generics.ListCreateAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    pagination_class = BookCopyPagination


class BookCopyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
