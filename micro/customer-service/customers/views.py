from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

@csrf_exempt
def customer_list_create(request):
    if request.method == 'GET':
        customers = list(Customer.objects.values())
        return JsonResponse(customers, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        return JsonResponse(customer.to_dict(), status=201)

@csrf_exempt
def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse(customer.to_dict())