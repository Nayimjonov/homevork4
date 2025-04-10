from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='list'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book_detail'),
]