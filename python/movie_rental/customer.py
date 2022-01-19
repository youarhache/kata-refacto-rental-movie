from nis import match
from tokenize import Double
from typing import List
from python.movie_rental.movie import Movie, PriceCodes
from python.movie_rental.rental import Rental


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

        for each in self._rentals:
            this_amount = 0.0

            #//determine amounts for each line
            match each.movie.price_code:
                case PriceCodes.REGULAR:
                    this_amount += 2
                    if each.days_rented > 2:
                        this_amount += (each.days_rented - 2) * 1.5
                case PriceCodes.NEW_RELEASE:
                    this_amount += each.days_rented * 3
                case PriceCodes.CHILDRENS:
                    this_amount += 1.5
                    if each.days_rented > 3:
                        this_amount += (each.days_rented - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            if (each.movie.price_code == PriceCodes.NEW_RELEASE) and each.days_rented > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.movie.title + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        return result