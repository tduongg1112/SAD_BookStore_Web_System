from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('create/', views.cart_create, name='cart_create'),
    path('update/<int:pk>/', views.cart_update, name='cart_update'),
    path('delete/<int:pk>/', views.cart_delete, name='cart_delete'),
    path('items/', views.cartitem_list, name='cartitem_list'),
    path('items/create/', views.cartitem_create, name='cartitem_create'),
    path('items/update/<int:pk>/', views.cartitem_update, name='cartitem_update'),
    path('items/delete/<int:pk>/', views.cartitem_delete, name='cartitem_delete'),
]
