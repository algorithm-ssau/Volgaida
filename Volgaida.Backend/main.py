from typing import List

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from Dto.CategoryDto import CategoryDto
from Dto.ProductFullDto import ProductFullDto
from Dto.ProductShortDto import ProductShortDto

# router = APIRouter(prefix='/api')

app = FastAPI(
    title='Valgoida',
    message='Hello Volgaida'
)
# app.include_router(router)

category_table = [
    {'id': 1, 'name': 'Барная карта', 'image': '1112'},
    {'id': 2, 'name': 'Салат', 'image': '1112'},
    {'id': 3, 'name': 'Напиток', 'image': '1112'},
    {'id': 4, 'name': 'Горячее блюдо', 'image': '1112'},
    {'id': 5, 'name': 'Закуска', 'image': '1112'},
    {'id': 6, 'name': 'Десерт', 'image': '1112'}
]

products_full_table = [
    {'id': 1, 'name': 'borsch', 'image': '1112', 'description': 'борщ', 'price': 200},
    {'id': 2, 'name': 'steak', 'image': '1112', 'description': 'стейк', 'price': 300},
    {'id': 3, 'name': 'caesar_salad', 'image': '1112', 'description': 'салат цезарь', 'price': 250},
    {'id': 4, 'name': 'french_fries', 'image': '1112', 'description': 'картофель фри', 'price': 105}
]

products_short_table = [
    {'id': 1, 'name': 'borsch', 'image_compressed': '1112', 'category_id': 4},
    {'id': 2, 'name': 'steak', 'image_compressed': '1112', 'category_id': 4},
    {'id': 3, 'name': 'caesar_salad', 'image_compressed': '1112', 'category_id': 2},
    {'id': 4, 'name': 'french_fries', 'image_compressed': '1112', 'category_id': 5}
]


@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({'detail': 'Entity not found'})
    )


@app.get('/categories', response_model=List[CategoryDto])
def get_categories():
    return [category for category in category_table]


@app.get('/products/{product_id}', response_model=ProductFullDto)
def get_product_by_id(product_id: int = 1):
    return [product for product in products_full_table if product.get('id') == product_id][0]


@app.get('/products/category/{category_id}', response_model=List[ProductShortDto])
def get_products_by_category(category_id: int = 1):
    return [product for product in products_short_table if product.get('category_id') == category_id]
