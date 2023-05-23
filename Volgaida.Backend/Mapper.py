from Dto.ProductFullDto import ProductFullDto
from Dto.ProductShortDto import ProductShortDto
from Models.Category import Category
from Models.Product import Product


def model_to_product_short(product: Product):
    product_short = ProductShortDto()
    product_short.name = product.name
    product_short.id = product.id
    product_short.image_compressed = compress_image(product.image)
    return product_short


def model_to_product_full(product: Product):
    product_full = ProductFullDto()
    product_full.name = product.name
    product_full.price = product.price
    product_full.description = product.description
    product_full.image = product.image
    return product_full


def model_to_category(category: Category):
    category_dto = Category()
    category_dto.name = category.name
    category_dto.id = category.id
    category_dto.image = category.image
    return category_dto


def compress_image(image: str):
    return image
