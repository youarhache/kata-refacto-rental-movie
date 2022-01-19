from python.movie_rental.movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented: int) -> None:
        self.movie = movie
        self.days_rented = days_rented
