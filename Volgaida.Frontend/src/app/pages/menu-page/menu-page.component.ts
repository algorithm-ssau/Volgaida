import {Component, OnInit} from '@angular/core';
import {HttpCategoryMockService} from "../../core/mocks/http-category-mock.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-menu-page',
  templateUrl: './menu-page.component.html',
  styleUrls: ['./menu-page.component.css']
})
export class MenuPageComponent implements OnInit {

  constructor(
    readonly categoryService: HttpCategoryMockService,
    public router: Router
  ) {
  }

  ngOnInit(): void {
  }

  navigateOnCategory(categoryId: number): void {
    this.router.navigate(
      ['/category', categoryId]
    );
  }
}
