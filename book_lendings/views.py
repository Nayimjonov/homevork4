from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
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

class BookLendingReturnView(generics.RetrieveAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer

    def get(self, request, *args, **kwargs):
        lending = self.get_object()
        if lending.status == 'returned':
            return Response({"detail": "This book is already returned."}, status=status.HTTP_400_BAD_REQUEST)
        lending.status = 'returned'
        lending.returned_date = timezone.now()
        lending.save()

        return Response(self.get_serializer(lending).data, status=status.HTTP_200_OK)

class BookLendingOverdueView(generics.RetrieveAPIView):
    queryset = BookLending.objects.all()
    serializer_class = BookLendingSerializer

    def get(self, request, *args, **kwargs):
        lending = self.get_object()
        if lending.due_date < timezone.now() and lending.status != 'returned':
            lending.status = 'overdue'
            lending.save()

        return Response(self.get_serializer(lending).data, status=status.HTTP_200_OK)