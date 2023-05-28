import {Component, Inject, OnInit, TemplateRef} from '@angular/core';
import {TuiDialogContext, TuiDialogService} from "@taiga-ui/core";

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {
  constructor(@Inject(TuiDialogService) private readonly dialogs: TuiDialogService) { }

  ngOnInit(): void {
  }

  openMobileMenu(content: TemplateRef<TuiDialogContext>) {
    this.dialogs
      .open(content, {
        closeable: false,
        size: "page"
      })
      .subscribe();
  }
}
