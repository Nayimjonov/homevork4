from rest_framework.pagination import PageNumberPagination


class BookLendingPagination(PageNumberPagination):
    page_size = 10