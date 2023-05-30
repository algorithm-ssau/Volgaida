import {Inject, Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {ProductFullDto} from "../dto/ProductFullDto";
import {catchError, Observable, throwError} from "rxjs";
import {TuiAlertService} from "@taiga-ui/core";
import {ProductShortDto} from "../dto/ProductShortDto";

@Injectable({
  providedIn: 'root'
})
export class HttpProductService {
  private readonly url = '/' + 'products/';

  constructor(private readonly http: HttpClient, @Inject(TuiAlertService) private readonly alerts: TuiAlertService) {
  }

  private errorHandler(error: HttpErrorResponse) {
    this.alerts
      .open(error.message, {label: 'Error!'})
      .subscribe();

    return throwError(() => error.message)
  }

  getById(productId: number): Observable<ProductFullDto> {
    return this.http.get<ProductFullDto>(this.url + productId)
      .pipe(
        catchError(this.errorHandler.bind(this))
      )
  }

  getByCategories(categoryId: number): Observable<ProductShortDto[]> {
    return this.http.get<ProductShortDto[]>(this.url + 'category/' + categoryId)
      .pipe(
        catchError(this.errorHandler.bind(this))
      )
  }

  getImageUrl(productId: number) : string {
    return this.url + productId + '/image'
  }
}
