from rest_framework import generics
from .models import BookLending
from .serializers import BookLendingListSerializer, BookLendingSerializer
from .pagination import BookLendingPagination

class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    pagination_class = BookLendingPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookLendingListSerializer
        return BookLendingSerializer


class BookLendingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = BookLending.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookLendingListSerializer
        return BookLendingSerializer
