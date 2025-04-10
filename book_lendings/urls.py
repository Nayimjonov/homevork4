from django.urls import path
from . import views


urlpatterns = [
    path('lendings/', views.BookLendingListCreateView.as_view(), name='list'),
    path('lendings/<int:pk>/', views.BookLendingRetrieveUpdateAPIView.as_view(), name='lendings_detail'),
]