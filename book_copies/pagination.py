from rest_framework.pagination import PageNumberPagination


class BookCopyPagination(PageNumberPagination):
    page_size = 10


