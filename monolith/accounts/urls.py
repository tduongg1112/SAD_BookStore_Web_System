from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('update/<str:pk>/', views.customer_update, name='customer_update'),
    path('delete/<str:pk>/', views.customer_delete, name='customer_delete'),
]
