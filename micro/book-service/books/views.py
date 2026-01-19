from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "stock": self.stock
        }

@csrf_exempt
def book_list_create(request):
    if request.method == 'GET':
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            price=data['price'],
            stock=data['stock']
        )
        return JsonResponse(book.to_dict(), status=201)

@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse(book.to_dict())