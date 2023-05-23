import {ProductFullDto} from "../dto/ProductFullDto";
import {ProductShortDto} from "../dto/ProductShortDto";
import {CategoryDto} from "../dto/CategoryDto";

export const ProductFullMock: ProductFullDto = {
  name: 'Куриный бутерброд на деревянной доске',
  price: 1500.5,
  description: 'Курица деревенская, белый хлеб, помидоры, листья салата, плавленный сыр, огурцы, соус',
  weight: 300,
  proteins: 7,
  fats: 9,
  carbohydrates: 17,
  image: 'assets/images/mocks/mock-product.jpg'
}

export const ProductsShortMock: ProductShortDto[] = [
  {
    id: 1,
    name: 'Product_1',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 2,
    name: 'Product_2',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 3,
    name: 'Product_3',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 4,
    name: 'Product_4',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 5,
    name: 'Product_5',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 6,
    name: 'Product_6',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },{
    id: 7,
    name: 'Product_7',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 8,
    name: 'Product_8',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 9,
    name: 'Product_9',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 10,
    name: 'Product_10',
    image_compressed: 'assets/images/mocks/mock-product.jpg'
  }
]

export const CategoriesMock: CategoryDto[] = [
  {
    id: 1,
    name: 'Салаты',
    image: 'assets/images/mocks/mock-product.jpg'
  },
  {
    id: 2,
    name: 'Горячие блюда',
    image: 'assets/images/mocks/mock-rectangle.png'
  },
  {
    id: 3,
    name: 'Напитки',
    image: 'assets/images/mocks/mock-rectangle.png'
  },
  {
    id: 4,
    name: 'Барная карта',
    image: 'assets/images/mocks/mock-rectangle.png'
  },
  {
    id: 5,
    name: 'Закуски',
    image: 'assets/images/mocks/mock-rectangle.png'
  },
  {
    id: 6,
    name: 'Дессерты',
    image: 'assets/images/mocks/mock-rectangle.png'
  }
]