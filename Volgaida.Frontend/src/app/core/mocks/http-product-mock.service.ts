import {Injectable} from '@angular/core';
import {Observable, of} from "rxjs";
import {ProductFullDto} from "../dto/ProductFullDto";
import {ProductShortDto} from "../dto/ProductShortDto";
import {ProductFullMock, ProductsShortMock} from "./HttpConstMocks";

@Injectable({
  providedIn: 'root'
})
export class HttpProductMockService {

  constructor() {
  }

  getById(productId: number): Observable<ProductFullDto> {
    return of(ProductFullMock)
  }

  getByCategories(categoryId: number): Observable<ProductShortDto[]> {
    return of(ProductsShortMock)
  }
}