import {Inject, Injectable} from '@angular/core';
import {environment} from "../../../environments/environment";
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {TuiAlertService} from "@taiga-ui/core";
import {catchError, Observable, of, throwError} from "rxjs";
import {CategoryDto} from "../dto/CategoryDto";

@Injectable({
  providedIn: 'root'
})
export class HttpCategoryService {
  private readonly url = environment.API_URL + 'categories/';

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

  getImageById(categoryId: number): Observable<Blob> {
    return this.http.get(this.url + categoryId + '/image', {responseType: 'blob'})
      .pipe(
        catchError(this.errorHandler.bind(this))
      )
  }
}
