import {ProductFullDto} from "../dto/ProductFullDto";
import {ProductShortDto} from "../dto/ProductShortDto";
import {CategoryDto} from "../dto/CategoryDto";

export const ProductFullMock: ProductFullDto = {
  name: 'string',
  price: 1500.5,
  description: 'string',
  image: 'string'
}

export const ProductsShortMock: ProductShortDto[] = [
  {
    id: 1,
    name: 'string',
    image_compressed: 'string'
  },
  {
    id: 1,
    name: 'string',
    image_compressed: 'string'
  },
  {
    id: 1,
    name: 'string',
    image_compressed: 'string'
  }
]

export const CategoriesMock: CategoryDto[] = [
  {
    id: 1,
    name: 'string',
    image: 'string'
  },
]
