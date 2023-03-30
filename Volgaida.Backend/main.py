from typing import List

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from Model.Product import Product

app = FastAPI(
    title='Valgoida'
)

products_db = [
    {'id': 1, 'name': 'borsch', 'price': 200, 'tagList': [
        'soup'
    ]},
    {'id': 2, 'name': 'steak', 'price': 300, 'tagList': [
        'meat'
    ]},
    {'id': 3, 'name': 'barbecue', 'price': 250, 'tagList': [
        'meat'
    ]},
    {'id': 4, 'name': 'french_fries', 'price': 105, 'tagList': [
        'garnish'
    ]}
]


@app.exception_handler(ValidationError)
async def validation_exception_handler(exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'detail': exc.errors()}),
    )


@app.get('/products')
def get_product(product_id: int = 1):
    return [product for product in products_db if product.get('id') == product_id]


@app.post('/')
def add_trades(products: List[Product]):
    products_db.extend(products)
    return {'status': 200, 'data': products_db}
