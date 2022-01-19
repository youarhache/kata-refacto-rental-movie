from abc import abstractmethod, ABC
from typing import Type
from movie_rental.movie import Movie, PriceCodes


class Rental(ABC):
    movie: Movie
    days_rented: int

    @abstractmethod
    def __init__(self, movie: Movie, days_rented: int) -> None:
        self.movie = movie
        self.days_rented = days_rented

    @abstractmethod
    def get_price(self) -> float:
        """return the cost of the current rental"""

    @abstractmethod
    def get_frequent_renter_points(self) -> int:
        """return the frequent renter points earned for this rental"""


class RegularRental(Rental):
    def __init__(self, movie: Movie, days_rented: int) -> None:
        super().__init__(movie, days_rented)

    def get_price(self) -> float:
        return 2.0 + self._get_long_rental_additional_fees()

    def _get_long_rental_additional_fees(self) -> float:
        if self.days_rented <= 2:
            return 0
        return (self.days_rented - 2) * 1.5

    def get_frequent_renter_points(self) -> int:
        return 1


class NewReleaseRental(Rental):
    def __init__(self, movie: Movie, days_rented: int) -> None:
        super().__init__(movie, days_rented)

    def get_price(self) -> float:
        return self.days_rented * 3.0

    def get_frequent_renter_points(self) -> int:
        frequent_renter_points = 1 + self._get_bonus_points()
        return frequent_renter_points

    def _get_bonus_points(self) -> int:
        return int(self.days_rented > 1)


class ChildrenMovieRental(Rental):
    def __init__(self, movie: Movie, days_rented: int) -> None:
        super().__init__(movie, days_rented)

    def get_price(self) -> float:
        return 1.5 + self._get_long_rental_additional_fees()

    def _get_long_rental_additional_fees(self) -> float:
        if self.days_rented <= 3:
            return 0
        return (self.days_rented - 3) * 1.5

    def get_frequent_renter_points(self) -> int:
        return 1


def rental_factory_method(movie: Movie, days_rented: int) -> Rental:
    RENTAL_FACTORY_MAPPING: dict[PriceCodes, Type[Rental]] = {
        PriceCodes.REGULAR: RegularRental,
        PriceCodes.NEW_RELEASE: NewReleaseRental,
        PriceCodes.CHILDREN: ChildrenMovieRental,
    }

    rental_class: Type[Rental] = RENTAL_FACTORY_MAPPING[movie.price_code]
    return rental_class(movie, days_rented)
