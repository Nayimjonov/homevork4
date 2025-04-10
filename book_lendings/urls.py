from django.urls import path
from . import views

urlpatterns = [
    path('lendings/', views.BookLendingListCreateView.as_view(), name='list'),
    path('lendings/<int:pk>/', views.BookLendingRetrieveUpdateAPIView.as_view(), name='lendings_detail'),
    path('lendings/<int:pk>/return/', views.BookLendingReturnView.as_view(), name='book_lending_return'),
    path('lendings/<int:pk>/overdue/', views.BookLendingOverdueView.as_view(), name='book_lending_overdue'),
]
