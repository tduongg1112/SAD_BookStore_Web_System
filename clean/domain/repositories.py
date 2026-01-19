# clean/domain/repositories.py
from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import Customer, Book, Cart, CartItem

class ICustomerRepository(ABC):
    @abstractmethod
    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Customer]:
        pass

    @abstractmethod
    def create(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def delete(self, customer_id: str) -> None:
        pass

class IBookRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def create(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass

class ICartRepository(ABC):
    @abstractmethod
    def get_by_customer_id(self, customer_id: str) -> Optional[Cart]:
        pass

    @abstractmethod
    def create(self, cart: Cart) -> None:
        pass
    
    @abstractmethod
    def add_item(self, cart_id: int, book: Book, quantity: int) -> None:
        pass
        
    @abstractmethod
    def remove_item(self, item_id: int) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Cart]:
        pass
