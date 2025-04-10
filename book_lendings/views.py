from rest_framework import generics
from .models import BookLending
from .serializers import BookLendingSerializer
from .pagination import BookLendingPagination

class BookLendingListCreateView(generics.ListCreateAPIView):
    queryset = BookLending.objects.all()
    pagination_class = BookLendingPagination
    serializer_class = BookLendingSerializer


class BookLendingRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer