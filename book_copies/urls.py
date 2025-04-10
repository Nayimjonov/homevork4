from django.urls import path
from . import views


urlpatterns = [
    path('copies/', views.BookCopyListCreateView.as_view(), name='list'),
    path('copies/<int:pk>/', views.BookCopyRetrieveUpdateDestroyView.as_view(), name='copies_detail'),
]