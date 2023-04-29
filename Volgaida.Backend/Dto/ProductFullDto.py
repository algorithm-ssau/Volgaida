from pydantic import BaseModel


class ProductFullDto(BaseModel):
    name: str
    price: float
    description: str
    image: str
