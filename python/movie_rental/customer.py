from nis import match
from tokenize import Double
from typing import List
from movie_rental.movie import PriceCodes
from movie_rental.rental import Rental


class Customer:

    name: str
    _rentals: List[Rental]

    def __init__(self, name: str) -> None:
        self.name = name
        self._rentals = []

    def add_rental(self, arg: Rental) -> None:
        self._rentals.append(arg)

    def statement(self) -> str:
        total_amount = 0.0
        frequent_renter_points = 0
        result = "Rental Record for " + self.name + "\n"

        for rental in self._rentals:
            this_amount = rental.get_price()
            total_amount += this_amount

            # add frequent renter points
            frequent_renter_points += rental.get_frequent_renter_points()

            # show figures for this rental
            result += "\t" + rental.movie.title + "\t" + str(this_amount) + "\n"

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += (
            "You earned " + str(frequent_renter_points) + " frequent renter points"
        )

        return result
