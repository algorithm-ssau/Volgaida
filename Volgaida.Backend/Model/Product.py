from enum import Enum
from typing import List

from pydantic import BaseModel


class ProductTag(Enum):
    alcohol = "alcohol"
    soup = "soup"
    pizza = "pizza"
    pasta = "pasta"
    garnish = "garnish"
    meat = "meat"


class Product(BaseModel):
    id: int
    name: str
    price: float
    tagList: List[ProductTag]
