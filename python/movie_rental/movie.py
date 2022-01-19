from enum import Enum
from dataclasses import dataclass


class PriceCodes(Enum):
    CHILDRENS = 2
    NEW_RELEASE = 1
    REGULAR = 0


@dataclass
class Movie:
    title: str
    price_code: PriceCodes
