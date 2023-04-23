from pydantic import BaseModel

from Model.ProductTag import ProductTag


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    image_base64: str
    tagList: ProductTag
