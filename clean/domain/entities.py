# clean/domain/entities.py
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Customer:
    id: str
    name: str
    email: str
    password: str

@dataclass
class Book:
    id: Optional[int]
    title: str
    author: str
    price: float
    stock: int

@dataclass
class CartItem:
    id: Optional[int]
    book: Book
    quantity: int

@dataclass
class Cart:
    id: Optional[int]
    customer_id: str
    created_at: datetime
    items: List[CartItem]
