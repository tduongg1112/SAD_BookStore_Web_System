from django.urls import path
from .views import customer_list_create, customer_detail

urlpatterns = [
    path('api/customers/', customer_list_create),
    path('api/customers/<str:pk>/', customer_detail),
]
