# clean/usecases/book_usecases.py
from typing import List
from domain.entities import Book
from domain.repositories import IBookRepository

class ListBooksUseCase:
    def __init__(self, repository: IBookRepository):
        self.repository = repository

    def execute(self) -> List[Book]:
        return self.repository.get_all()

class CreateBookUseCase:
    def __init__(self, repository: IBookRepository):
        self.repository = repository

    def execute(self, title: str, author: str, price: float, stock: int) -> None:
        book = Book(id=None, title=title, author=author, price=price, stock=stock)
        self.repository.create(book)
