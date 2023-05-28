import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";
import {HttpCategoryService} from "../../core/http/http-category.service";
import {Observable} from "rxjs";
import {CategoryDto} from "../../core/dto/CategoryDto";

@Component({
  selector: 'app-menu-page',
  templateUrl: './menu-page.component.html',
  styleUrls: ['./menu-page.component.css']
})
export class MenuPageComponent implements OnInit {

  public categories: CategoryDto[] | undefined;

  constructor(
    readonly categoryService: HttpCategoryService,
    public router: Router
  ) {
  }

  ngOnInit(): void {
    this.categoryService.getAll().subscribe(categories => {
      this.categories = categories
    });
  }

  navigateOnCategory(categoryId: number): void {
    this.router.navigate(
      ['/category', categoryId]
    );
  }
}
