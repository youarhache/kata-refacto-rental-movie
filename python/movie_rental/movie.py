from enum import Enum


class PriceCodes(Enum):
    CHILDREN = 2
    NEW_RELEASE = 1
    REGULAR = 0


class Movie:
    def __init__(self, title: str, price_code: PriceCodes) -> None:
        self.title = title
        self.price_code = price_code
