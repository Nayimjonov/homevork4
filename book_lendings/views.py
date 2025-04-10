from rest_framework import generics
from .models import BookLending
from .serializers import BookLendingListSerializer
from .pagination import BookLendingPagination


class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingListSerializer
    pagination_class =BookLendingPagination

class BookLendingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingListSerializer

