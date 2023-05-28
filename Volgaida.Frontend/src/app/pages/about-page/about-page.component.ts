import {Component, OnInit} from '@angular/core';

import {ImageSize} from "../../core/ImageSize";

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
