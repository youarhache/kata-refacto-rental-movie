class Movie:

    CHILDRENS: int = 2
    NEW_RELEASE: int = 1
    REGULAR: int = 0

    def __init__(self, title: str, price_code: int) -> None:
        self._title = title
        self._price_code = price_code

    def get_price_code(self) -> int:
        return self._price_code

    def set_price_code(self, arg: int) -> None:
        self._price_code = arg

    def get_title(self) -> str:
        return self._title
