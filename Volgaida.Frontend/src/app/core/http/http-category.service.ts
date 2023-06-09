import {Inject, Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {TuiAlertService} from "@taiga-ui/core";
import {catchError, Observable, throwError} from "rxjs";
import {CategoryDto} from "../dto/CategoryDto";

@Injectable({
  providedIn: 'root'
})
export class HttpCategoryService {
  private readonly url = '/api/' + 'categories/';

  constructor(private readonly http: HttpClient, @Inject(TuiAlertService) private readonly alerts: TuiAlertService) {
  }

  private errorHandler(error: HttpErrorResponse) {
    this.alerts
      .open(error.message, {label: 'Error!'})
      .subscribe();

    return throwError(() => error.message)
  }

  getAll(): Observable<CategoryDto[]> {
    return this.http.get<CategoryDto[]>(this.url)
      .pipe(
        catchError(this.errorHandler.bind(this))
      )
  }

  getNameById(categoryId: number): Observable<string> {
    return this.http.get<string>(this.url + categoryId + '/name')
      .pipe(
        catchError(this.errorHandler.bind(this))
      )
  }

  getImageUrl(categoryId: number): string {
    return this.url + categoryId + '/image'
  }
}
