from python.movie_rental.movie import Movie


class Rental:
    def __init__(self, movie: Movie, days_rented: int) -> None:
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self) -> int:
        return self._days_rented

    def get_movie(self) -> Movie:
        return self._movie
