from django.db import models

class CustomerModel(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'clean_customer'

class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

    class Meta:
        db_table = 'clean_book'

class CartModel(models.Model):
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clean_cart'

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'clean_cartitem'