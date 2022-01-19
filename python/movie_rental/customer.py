from nis import match
from tokenize import Double
from typing import List
from python.movie_rental.movie import Movie
from python.movie_rental.rental import Rental


class Customer:

    _name: str
    _rentals: List[Rental]

    def __init__(self, name: str) -> None:
        self._name = name
        self._rentals = []

    def add_rental(self, arg: Rental) -> None:
        self._rentals.append(arg)

    def get_name(self) -> str:
        return self._name

    def statement(self) -> str:
        total_amount = 0.0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self._rentals:
            this_amount = 0.0

            #//determine amounts for each line
            match each.get_movie().get_price_code():
                case Movie.REGULAR:
                    this_amount += 2
                    if each.get_days_rented() > 2:
                        this_amount += (each.get_days_rented() - 2) * 1.5
                case Movie.NEW_RELEASE:
                    this_amount += each.get_days_rented() * 3
                case Movie.CHILDRENS:
                    this_amount += 1.5
                    if each.get_days_rented() > 3:
                        this_amount += (each.get_days_rented() - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and each.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        return result