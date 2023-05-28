from pydantic import BaseModel


class ProductShortDto(BaseModel):
    id: int
    name: str
