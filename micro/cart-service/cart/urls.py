from django.urls import path
from .views import cart_create, cart_add_item, cart_detail

urlpatterns = [
    path('api/carts/', cart_create),
    path('api/carts/<int:pk>/', cart_detail),
    path('api/carts/<int:cart_id>/items/', cart_add_item),
]
