from django.urls import path
from . import views


urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view(), name='list'),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroy.as_view(), name='author_detail'),
    path('authors/<int:pk>/books/', views.AuthorBookListView.as_view(), name='book_list'),
]