import {Component, Inject, OnInit, TemplateRef} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {switchMap} from "rxjs";
import {HttpProductMockService} from "../../core/mocks/http-product-mock.service";
import {ProductShortDto} from "../../core/dto/ProductShortDto";
import {HttpCategoryMockService} from "../../core/mocks/http-category-mock.service";
import {TuiDialogContext, TuiDialogService, TuiDialogSize} from "@taiga-ui/core";
import {ProductFullDto} from "../../core/dto/ProductFullDto";

@Component({
  selector: 'app-category-page',
  templateUrl: './category-page.component.html',
  styleUrls: ['./category-page.component.css']
})
export class CategoryPageComponent implements OnInit {
  products: ProductShortDto[] | undefined;
  title: string | undefined;

  selectedProduct: ProductFullDto | undefined;

  constructor(
    private categoryService: HttpCategoryMockService,
    private productService: HttpProductMockService,
    private activatedRoute: ActivatedRoute,
    @Inject(TuiDialogService) private readonly dialogs: TuiDialogService
  ) {
  }

  ngOnInit(): void {
    this.activatedRoute.paramMap.pipe(
      switchMap(params => params.getAll('id'))
    )
      .subscribe(id => {
        this.productService.getByCategories(+id).subscribe(products => {
          this.products = products
        })
        this.categoryService.getNameById(+id).subscribe(name => {
          this.title = name
        })
      });
  }

  onClick(
    product: ProductShortDto,
    content: TemplateRef<TuiDialogContext>,
    size: TuiDialogSize,
  ): void {
    this.productService.getById(product.id).subscribe(productDto => {
      this.selectedProduct = productDto
    })

    this.dialogs
      .open(content, {
        size,
      })
      .subscribe();
  }
}
