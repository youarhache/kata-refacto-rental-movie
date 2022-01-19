from dataclasses import dataclass
from python.movie_rental.movie import Movie


@dataclass
class Rental:
    movie: Movie
    days_rented: int
