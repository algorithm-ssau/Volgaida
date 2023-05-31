from typing import List

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from Dto.CategoryDto import CategoryDto
from Dto.ProductFullDto import ProductFullDto
from Dto.ProductShortDto import ProductShortDto
from BL.database import select_categories, select_category_image_by_id, select_full_product_by_id, \
    select_short_products, select_product_image_by_id, select_category_name_by_id, select_short_products_by_category, \
    init_db

# uvicorn main:app --reload

app = FastAPI(
    title='Volgaida',
    message='Hello Volgaida'
)

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({'detail': 'Entity not found'})
    )


@app.get('/api/categories', response_model=List[CategoryDto])
async def get_categories():
    categories = select_categories()
    categories_dto = []
    for category in categories:
        categories_dto.append(
            CategoryDto(id=category[0],
                        name=category[1],
                        )
        )
    return categories_dto


@app.get('/api/categories/{category_id}/name', response_model=str)
async def get_category_name_by_id(category_id: int = 1):
    category = select_category_name_by_id(category_id)
    return category


@app.get('/api/categories/{category_id}/image')
async def get_category_image_by_id(category_id: int):
    category_image = select_category_image_by_id(category_id)
    return Response(content=category_image, media_type="image/jpg")


@app.get('/api/products', response_model=List[ProductShortDto])
async def get_products():
    products = select_short_products()
    products_dto = []
    for product in products:
        products_dto.append(ProductShortDto(id=product[0], name=product[1]))
    return products_dto


@app.get('/api/products/category/{category_id}', response_model=List[ProductShortDto])
async def get_products_by_category(category_id: int):
    products = select_short_products_by_category(category_id)
    products_dto = []
    for product in products:
        products_dto.append(ProductShortDto(id=product[0], name=product[1]))
    return products_dto


@app.get('/api/products/{product_id}', response_model=ProductFullDto)
async def get_product_by_id(product_id: int):
    products = select_full_product_by_id(product_id)
    product_full = []
    for product in products:
        product_full.append(ProductFullDto(id=product[0], name=product[1], ingredients=product[2],
                                           pfc=product[3], weight=product[4], price=product[5]))
    return product_full[0]


@app.get('/api/products/{product_id}/image')
async def get_product_image_by_id(product_id: int):
    product_image = select_product_image_by_id(product_id)
    return Response(content=product_image, media_type="image/jpg")
