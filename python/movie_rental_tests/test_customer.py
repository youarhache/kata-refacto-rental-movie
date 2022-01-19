from os import name
from python.movie_rental.customer import Customer
from python.movie_rental.movie import Movie
from customer_builder import CustomerBuilder
from python.movie_rental.rental import Rental


def test_customer():
    customer = CustomerBuilder().build()

    assert isinstance(customer, Customer)


def test_add_rental():
    customer = CustomerBuilder().with_name("Julia").build()
    movie1 = Movie("Gone with the Wind", Movie.REGULAR)
    rental1 = Rental(movie1, days_rented=3)
    customer.add_rental(rental1)
    assert customer._rentals == [rental1]


def test_get_name():
    customer = Customer(name="David")
    assert customer.get_name() == "David"


def test_statement_for_regular_movie():
    movie1 = Movie("Gone with the Wind", Movie.REGULAR)
    rental1 = Rental(movie1, days_rented=3)
    customer = CustomerBuilder().with_name(name="Sallie").with_rentals(rental1).build()
    expected = (
        "Rental Record for Sallie\n"
        + "\tGone with the Wind\t3.5\n"
        + "Amount owed is 3.5\n"
        + "You earned 1 frequent renter points"
    )

    statement = customer.statement()

    assert statement == expected


def test_statement_for_new_release_movie():
    movie1 = Movie("Star Wars", Movie.NEW_RELEASE)
    rental1 = Rental(movie1, days_rented=3)
    customer = CustomerBuilder().with_name(name="Sallie").with_rentals(rental1).build()
    expected = (
        "Rental Record for Sallie\n"
        + "\tStar Wars\t9.0\n"
        + "Amount owed is 9.0\n"
        + "You earned 2 frequent renter points"
    )

    statement = customer.statement()

    assert statement == expected


def test_statement_for_children_movie():
    movie1 = Movie("Madagascar", Movie.CHILDRENS)
    rental1 = Rental(movie1, days_rented=3)
    customer = CustomerBuilder().with_name(name="Sallie").with_rentals(rental1).build()
    expected = (
        "Rental Record for Sallie\n"
        + "\tMadagascar\t1.5\n"
        + "Amount owed is 1.5\n"
        + "You earned 1 frequent renter points"
    )

    statement = customer.statement()

    assert statement == expected


def test_statement_for_many_movies():
    movie1 = Movie("Madagascar", Movie.CHILDRENS)
    rental1 = Rental(movie1, days_rented=6)
    movie2 = Movie("Star Wars", Movie.NEW_RELEASE)
    rental2 = Rental(movie2, days_rented=2)
    movie3 = Movie("Gone with the Wind", Movie.REGULAR)
    rental3 = Rental(movie3, days_rented=8)
    customer = (
        CustomerBuilder()
        .with_name(name="David")
        .with_rentals(rental1, rental2, rental3)
        .build()
    )
    expected = (
        "Rental Record for David\n"
        + "\tMadagascar\t6.0\n"
        + "\tStar Wars\t6.0\n"
        + "\tGone with the Wind\t11.0\n"
        + "Amount owed is 23.0\n"
        + "You earned 4 frequent renter points"
    )

    statement = customer.statement()

    assert statement == expected


# TODO make test for price breaks in code.
