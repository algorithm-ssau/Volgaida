import {ProductFullDto} from "../dto/ProductFullDto";
import {ProductShortDto} from "../dto/ProductShortDto";
import {CategoryDto} from "../dto/CategoryDto";

export const ProductFullMock: ProductFullDto = {
  id: 1,
  name: 'Куриный бутерброд на деревянной доске',
  price: 1500.5,
  ingredients: 'Курица деревенская, белый хлеб, помидоры, листья салата, плавленный сыр, огурцы, соус',
  pfc: "10/12/5",
  weight: 100
}

export const ProductsShortMock: ProductShortDto[] = [
  {
    id: 1,
    name: 'Product_1',
  },
  {
    id: 2,
    name: 'Product_2',
  },
  {
    id: 3,
    name: 'Product_3',
  },
  {
    id: 4,
    name: 'Product_4',
  },
  {
    id: 5,
    name: 'Product_5'
  },
  {
    id: 6,
    name: 'Product_6'
  },{
    id: 7,
    name: 'Product_7'
  },
  {
    id: 8,
    name: 'Product_8'
  },
  {
    id: 9,
    name: 'Product_9'
  },
  {
    id: 10,
    name: 'Product_10'
  }
]

export const CategoriesMock: CategoryDto[] = [
  {
    id: 1,
    name: 'Салаты'
  },
  {
    id: 2,
    name: 'Горячие блюда'
  },
  {
    id: 3,
    name: 'Напитки'
  },
  {
    id: 4,
    name: 'Барная карта'
  },
  {
    id: 5,
    name: 'Закуски'
  },
  {
    id: 6,
    name: 'Дессерты'
  }
]
