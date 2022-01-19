from __future__ import annotations
from tokenize import Name

from typing import List
from movie_rental.customer import Customer
from movie_rental.rental import Rental


class CustomerBuilder:

    NAME: str = "Roberts"

    name: str
    rentals: List[Rental]

    def __init__(self) -> None:
        self.name = self.NAME
        self.rentals = []

    def with_name(self, name: str) -> CustomerBuilder:
        self.name = name
        return self

    def with_rentals(self, *rentals) -> CustomerBuilder:
        self.rentals.extend(rentals)
        return self

    def build(self) -> Customer:
        result = Customer(self.name)
        for rental in self.rentals:
            result.add_rental(rental)
        return result
