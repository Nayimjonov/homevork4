from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    page_size = 10

class BookCopyPagination(PageNumberPagination):
    page_size = 10
