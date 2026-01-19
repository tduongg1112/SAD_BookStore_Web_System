from django.urls import path
from .views import book_list_create, book_detail

urlpatterns = [
    path('api/books/', book_list_create),
    path('api/books/<int:pk>/', book_detail),
]
