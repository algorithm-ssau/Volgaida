import {Injectable} from '@angular/core';
import {Observable, of} from "rxjs";
import {CategoryDto} from "../dto/CategoryDto";
import {CategoriesMock} from "./HttpConstMocks";

@Injectable({
  providedIn: 'root'
})
export class HttpCategoryMockService {

  constructor() {
  }

  getAll(): Observable<CategoryDto[]> {
    return of(CategoriesMock)
  }

  getNameById(categoryId: number): Observable<string> {
    return of(CategoriesMock.filter(c => c.id == categoryId)[0].name)
  }
}