import { Component, OnInit } from '@angular/core';
import {ImageSize} from "../../../core/ImageSize";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {
  protected readonly ImageSize = ImageSize;

  constructor() { }

  ngOnInit(): void {
  }

}
