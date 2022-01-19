from dataclasses import dataclass
from typing import Type

from movie_rental.price_and_points_caclulators import (
    AbstractPointsCalculator,
    AbstractPriceCalculator,
)
from movie_rental.movie import PriceCodes
from movie_rental.price_and_points_caclulators import (
    ChildrenPriceCalculator,
    NewReleasePointsCalculation,
    NewReleasePriceCalculator,
    RegularPointsCalculation,
    RegularPriceCalculator,
)


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
