# clean/usecases/customer_usecases.py
from typing import List
from domain.entities import Customer
from domain.repositories import ICustomerRepository

class ListCustomersUseCase:
    def __init__(self, repository: ICustomerRepository):
        self.repository = repository

    def execute(self) -> List[Customer]:
        return self.repository.get_all()

class CreateCustomerUseCase:
    def __init__(self, repository: ICustomerRepository):
        self.repository = repository

    def execute(self, id: str, name: str, email: str, password: str) -> None:
        customer = Customer(id=id, name=name, email=email, password=password)
        self.repository.create(customer)
