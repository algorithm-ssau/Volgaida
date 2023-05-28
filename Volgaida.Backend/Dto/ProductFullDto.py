from pydantic import BaseModel


class ProductFullDto(BaseModel):
    name: str
    ingredients: str
    pfc: str
    weight: int
    price: int
