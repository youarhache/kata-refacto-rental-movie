from movie_rental.customer import Customer, print_statement
from movie_rental.movie import Movie, PriceCodes
from customer_builder import CustomerBuilder
from movie_rental.rental import Rental
from movie_rental.calulators_factory import calculators_factory_method


def test_customer():
    customer = CustomerBuilder().build()

    assert isinstance(customer, Customer)


def test_add_rental():
    customer = CustomerBuilder().with_name("Julia").build()
    days_rented = 3
    price_code = PriceCodes.REGULAR
    movie1 = Movie("Gone with the Wind", price_code)
    calculators = calculators_factory_method(price_code, days_rented)
    rental1 = Rental(movie1, days_rented, calculators)
    customer.add_rental(rental1)
    assert customer._rentals == [rental1]


def test_statement_for_regular_movie():
    days_rented = 3
    price_code = PriceCodes.REGULAR
    movie1 = Movie("Gone with the Wind", price_code)
    calculators = calculators_factory_method(price_code, days_rented)
    rental1 = Rental(movie1, days_rented, calculators)
    customer = CustomerBuilder().with_name(name="Sallie").with_rentals(rental1).build()
    expected = (
        "Rental Record for Sallie\n"
        + "\tGone with the Wind\t3.5\n"
        + "Amount owed is 3.5\n"
        + "You earned 1 frequent renter points"
    )

    statement = print_statement(customer)

    assert statement == expected


def test_statement_for_new_release_movie():
    days_rented = 3
    price_code = PriceCodes.NEW_RELEASE
    movie1 = Movie("Star Wars", price_code)
    calculators = calculators_factory_method(price_code, days_rented)
    rental1 = Rental(movie1, days_rented, calculators)
    customer = CustomerBuilder().with_name(name="Sallie").with_rentals(rental1).build()
    expected = (
        "Rental Record for Sallie\n"
        + "\tStar Wars\t9.0\n"
        + "Amount owed is 9.0\n"
        + "You earned 2 frequent renter points"
    )

    statement = print_statement(customer)

    assert statement == expected


def test_statement_for_children_movie():
    days_rented = 3
    price_code = PriceCodes.CHILDREN
    movie1 = Movie("Madagascar", price_code)
    calculators = calculators_factory_method(price_code, days_rented)
    rental1 = Rental(movie1, days_rented, calculators)
    customer = CustomerBuilder().with_name(name="Sallie").with_rentals(rental1).build()
    expected = (
        "Rental Record for Sallie\n"
        + "\tMadagascar\t1.5\n"
        + "Amount owed is 1.5\n"
        + "You earned 1 frequent renter points"
    )

    statement = print_statement(customer)

    assert statement == expected


def test_statement_for_many_movies():
    days_rented1 = 6
    price_code1 = PriceCodes.CHILDREN
    movie1 = Movie("Madagascar", price_code1)
    calculators1 = calculators_factory_method(price_code1, days_rented1)
    rental1 = Rental(movie1, days_rented1, calculators1)
    days_rented2 = 2
    price_code2 = PriceCodes.NEW_RELEASE
    movie2 = Movie("Star Wars", price_code2)
    calculators2 = calculators_factory_method(price_code2, days_rented2)
    rental2 = Rental(movie2, days_rented2, calculators2)
    days_rented3 = 8
    price_code3 = PriceCodes.REGULAR
    movie3 = Movie("Gone with the Wind", price_code3)
    calculators3 = calculators_factory_method(price_code3, days_rented3)
    rental3 = Rental(movie3, days_rented3, calculators3)
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

    statement = print_statement(customer)

    assert statement == expected


# TODO make test for price breaks in code.
