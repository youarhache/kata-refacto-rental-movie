from dataclasses import dataclass
from enum import Enum


class PriceCodes(Enum):
    CHILDREN = 2
    NEW_RELEASE = 1
    REGULAR = 0


@dataclass
class Movie:
    title: str
    price_code: PriceCodes
