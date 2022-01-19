from python.movie_rental.movie import Movie, PriceCodes


class Rental:
    def __init__(self, movie: Movie, days_rented: int) -> None:
        self.movie = movie
        self.days_rented = days_rented

    def get_amount(self):
        amount = 0.0
        match self.movie.price_code:
            case PriceCodes.REGULAR:
                amount += 2
                if self.days_rented > 2:
                    amount += (self.days_rented - 2) * 1.5
            case PriceCodes.NEW_RELEASE:
                amount += self.days_rented * 3
            case PriceCodes.CHILDRENS:
                amount += 1.5
                if self.days_rented > 3:
                    amount += (self.days_rented - 3) * 1.5
        return amount

    def get_frequent_renter_points(self):
        frequent_renter_points = 1
        if (
            self.movie.price_code == PriceCodes.NEW_RELEASE
        ) and self.days_rented > 1:
            frequent_renter_points += 1
        return frequent_renter_points