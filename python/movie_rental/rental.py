from dataclasses import dataclass
from movie_rental.price_and_points_caclulators import Calculators
from movie_rental.movie import Movie


@dataclass
class Rental:
    movie: Movie
    days_rented: int
    calculators: Calculators
