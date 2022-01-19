from abc import ABC, abstractmethod
from typing import Type
from dataclasses import dataclass
from movie_rental.movie import PriceCodes


class AbstractPriceCalculator(ABC):
    @abstractmethod
    def __init__(self, days_rented: int) -> None:
        ...

    @abstractmethod
    def get_price(self) -> float:
        """computes the price for the given rental"""


class RegularPriceCalculator(AbstractPriceCalculator):
    BASE_PRICE = 2.0
    DAILY_PRICE = 1.5
    ADDITIONAL_FEE_STARING_DAY = 2

    def __init__(self, days_rented: int) -> None:
        self.days_rented = days_rented

    def get_price(self) -> float:
        return self.BASE_PRICE + self._get_long_rental_additional_fees()

    def _get_long_rental_additional_fees(self) -> float:
        if self.days_rented <= self.ADDITIONAL_FEE_STARING_DAY:
            return 0
        return (self.days_rented - self.ADDITIONAL_FEE_STARING_DAY) * self.DAILY_PRICE


class ChildrenPriceCalculator(AbstractPriceCalculator):
    BASE_PRICE = 1.5
    DAILY_PRICE = 1.5
    ADDITIONAL_FEE_STARING_DAY = 3

    def __init__(self, days_rented: int) -> None:
        self.days_rented = days_rented

    def get_price(self) -> float:
        return self.BASE_PRICE + self._get_long_rental_additional_fees()

    def _get_long_rental_additional_fees(self) -> float:
        if self.days_rented <= self.ADDITIONAL_FEE_STARING_DAY:
            return 0
        return (self.days_rented - self.ADDITIONAL_FEE_STARING_DAY) * self.DAILY_PRICE


class NewReleasePriceCalculator(AbstractPriceCalculator):
    DAILY_PRICE = 3.0

    def __init__(self, days_rented: int) -> None:
        self.days_rented = days_rented

    def get_price(self) -> float:
        return self.days_rented * self.DAILY_PRICE


class AbstractPointsCalculator(ABC):
    @abstractmethod
    def __init__(self, days_rented: int) -> None:
        ...

    @abstractmethod
    def get_points(self) -> int:
        """computes the frequent renter points for the given rental"""


class RegularPointsCalculation(AbstractPointsCalculator):
    REGULAR_POINTS = 1

    def __init__(self, days_rented: int) -> None:
        self.days_rented = days_rented

    def get_points(self) -> int:
        return self.REGULAR_POINTS


class NewReleasePointsCalculation(AbstractPointsCalculator):
    REGULAR_POINTS = 1
    BONUS_POINTS_STARING_DAY = 1

    def __init__(self, days_rented: int) -> None:
        self.days_rented = days_rented

    def get_points(self) -> int:
        frequent_renter_points = self.REGULAR_POINTS + self._get_bonus_points()
        return frequent_renter_points

    def _get_bonus_points(self):
        return int(self.days_rented > self.BONUS_POINTS_STARING_DAY)


@dataclass
class Calculators:
    price_calculator: AbstractPriceCalculator
    points_calculator: AbstractPointsCalculator


@dataclass
class CalculatorsFactory:
    price_calculator_class: Type[AbstractPriceCalculator]
    points_calculator_class: Type[AbstractPointsCalculator]

    def __call__(self, days_rented: int) -> Calculators:
        return Calculators(
            self.price_calculator_class(days_rented),
            self.points_calculator_class(days_rented),
        )


def calculators_factory_method(price_code: PriceCodes, days_rented: int) -> Calculators:
    RENTAL_FACTORY_MAPPING: dict[PriceCodes, CalculatorsFactory] = {
        PriceCodes.REGULAR: CalculatorsFactory(
            RegularPriceCalculator, RegularPointsCalculation
        ),
        PriceCodes.NEW_RELEASE: CalculatorsFactory(
            NewReleasePriceCalculator, NewReleasePointsCalculation
        ),
        PriceCodes.CHILDREN: CalculatorsFactory(
            ChildrenPriceCalculator, RegularPointsCalculation
        ),
    }

    calculators_factory: CalculatorsFactory = RENTAL_FACTORY_MAPPING[price_code]
    return calculators_factory(days_rented)
