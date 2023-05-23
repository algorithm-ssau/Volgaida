import {Component, OnInit} from '@angular/core';

import {ImageSize} from "../../core/ImageSize";
import {HttpCategoryMockService} from "../../core/mocks/http-category-mock.service";

@Component({
  selector: 'app-about-page',
  templateUrl: './about-page.component.html',
  styleUrls: ['./about-page.component.css']
})
export class AboutPageComponent implements OnInit {
  protected readonly ImageSize = ImageSize;

  constructor() {
  }

  ngOnInit(): void {
  }
}
