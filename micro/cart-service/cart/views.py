from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# In microservices, we don't have direct FKs to other services' tables.
# We store IDs instead.

class Cart(models.Model):
    customer_id = models.CharField(max_length=50) # Reference ID from Customer Service
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "items": [item.to_dict() for item in self.items.all()]
        }

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book_id = models.IntegerField() # Reference ID from Book Service
    quantity = models.IntegerField()

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "quantity": self.quantity
        }

@csrf_exempt
def cart_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer_id = data.get('customer_id')
        
        # Verify customer exists (Communication with Customer Service)
        # In a real scenario, handle timeouts/errors
        # response = requests.get(f'http://localhost:8001/api/customers/{customer_id}/')
        # if response.status_code != 200:
        #    return JsonResponse({'error': 'Customer not found'}, status=400)

        cart = Cart.objects.create(customer_id=customer_id)
        return JsonResponse(cart.to_dict(), status=201)

@csrf_exempt
def cart_add_item(request, cart_id):
    if request.method == 'POST':
        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart not found'}, status=404)

        data = json.loads(request.body)
        book_id = data.get('book_id')
        quantity = data.get('quantity')

        # Verify book exists (Communication with Book Service)
        # response = requests.get(f'http://localhost:8002/api/books/{book_id}/')
        # if response.status_code != 200:
        #     return JsonResponse({'error': 'Book not found'}, status=400)

        item = CartItem.objects.create(cart=cart, book_id=book_id, quantity=quantity)
        return JsonResponse(cart.to_dict())

@csrf_exempt
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
        return JsonResponse(cart.to_dict())
    except Cart.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)