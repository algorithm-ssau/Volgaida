from typing import List

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from pydantic import ValidationError

from Dto.CategoryDto import CategoryDto
from Dto.ProductFullDto import ProductFullDto
from Dto.ProductShortDto import ProductShortDto
from Models.database import select_categories, select_category_image_by_id, select_full_product_by_id, \
    select_short_products, select_product_image_by_id, select_category_by_id, select_short_products_by_category

# uvicorn main:app --reload

app = FastAPI(
    title='Valgoida',
    message='Hello Volgaida'
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({'detail': 'Entity not found'})
    )


@app.get('/categories', response_model=List[CategoryDto])
def get_categories():
    categories = select_categories()
    categories_dto = []
    for category in categories:
        categories_dto.append(
            CategoryDto(id=category[0],
                        name=category[1],
                        )
        )
    return categories_dto


@app.get('/categories/{category_id}', response_model=str)
def get_category_by_id(category_id: int = 1):
    category = select_category_by_id(category_id)
    return category


@app.get('/categories/image/{id}',
         responses={
             200: {
                 "content": {"image/jpg": {}}
             }
         },
         response_class=Response)
def get_category_image_by_id(category_id: int = 1):
    category_image = select_category_image_by_id(category_id)
    return Response(content=category_image, media_type="image/jpg")


@app.get('/products', response_model=List[ProductShortDto])
def get_products():
    products = select_short_products()
    products_dto = []
    for product in products:
        products_dto.append(ProductShortDto(id=product[0], name=product[1]))
    return products_dto


@app.get('/products/category/{category_id}', response_model=List[ProductShortDto])
def get_products_by_category(category_id: int):
    products = select_short_products_by_category(category_id)
    products_dto = []
    for product in products:
        products_dto.append(ProductShortDto(id=product[0], name=product[1]))
    return products_dto


@app.get('/products/{product_id}', response_model=ProductFullDto)
def get_product_by_id(product_id: int = 1):
    products = select_full_product_by_id(product_id)
    product_full = []
    for product in products:
        product_full.append(ProductFullDto(id=product[0], name=product[1], ingredients=product[2],
                                           pfc=product[3], weight=product[4], price=product[5]))
    return product_full[0]


@app.get('/products/image/{id}',
         responses={
             200: {
                 "content": {"image/jpg": {}}
             }
         },
         response_class=Response)
def get_product_image_by_id(product_id: int = 1):
    product_image = select_product_image_by_id(product_id)
    return Response(content=product_image, media_type="image/jpg")
