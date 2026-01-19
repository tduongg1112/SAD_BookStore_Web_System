from typing import List, Optional
from domain.entities import Customer
from domain.repositories import ICustomerRepository
from core.models import CustomerModel

class DjangoCustomerRepository(ICustomerRepository):
    def get_all(self) -> List[Customer]:
        models = CustomerModel.objects.all()
        return [self._to_entity(m) for m in models]

    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        try:
            model = CustomerModel.objects.get(pk=customer_id)
            return self._to_entity(model)
        except CustomerModel.DoesNotExist:
            return None

    def create(self, customer: Customer) -> None:
        CustomerModel.objects.create(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            password=customer.password
        )

    def update(self, customer: Customer) -> None:
        CustomerModel.objects.filter(pk=customer.id).update(
            name=customer.name,
            email=customer.email,
            password=customer.password
        )

    def delete(self, customer_id: str) -> None:
        CustomerModel.objects.filter(pk=customer_id).delete()

    def _to_entity(self, model: CustomerModel) -> Customer:
        return Customer(
            id=model.id,
            name=model.name,
            email=model.email,
            password=model.password
        )

from domain.entities import Book
from domain.repositories import IBookRepository
from core.models import BookModel

class DjangoBookRepository(IBookRepository):
    def get_all(self) -> List[Book]:
        models = BookModel.objects.all()
        return [self._to_entity(m) for m in models]

    def get_by_id(self, book_id: int) -> Optional[Book]:
        try:
            model = BookModel.objects.get(pk=book_id)
            return self._to_entity(model)
        except BookModel.DoesNotExist:
            return None

    def create(self, book: Book) -> None:
        BookModel.objects.create(
            title=book.title,
            author=book.author,
            price=book.price,
            stock=book.stock
        )

    def update(self, book: Book) -> None:
        BookModel.objects.filter(pk=book.id).update(
            title=book.title,
            author=book.author,
            price=book.price,
            stock=book.stock
        )

    def delete(self, book_id: int) -> None:
        BookModel.objects.filter(pk=book_id).delete()

    def _to_entity(self, model: BookModel) -> Book:
        return Book(
            id=model.id,
            title=model.title,
            author=model.author,
            price=model.price,
            stock=model.stock
        )
