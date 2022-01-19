from enum import Enum


class PriceCodes(Enum):
    CHILDRENS = 2
    NEW_RELEASE = 1
    REGULAR = 0


class Movie:
    def __init__(self, title: str, price_code: PriceCodes) -> None:
        self._title = title
        self._price_code = price_code

    def get_price_code(self) -> PriceCodes:
        return self._price_code

    def set_price_code(self, arg: PriceCodes) -> None:
        self._price_code = PriceCodes

    def get_title(self) -> str:
        return self._title
