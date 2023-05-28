from pydantic import BaseModel


class ProductFullDto(BaseModel):
    id: int
    name: str
    ingredients: str
    pfc: str
    weight: int
    price: int
