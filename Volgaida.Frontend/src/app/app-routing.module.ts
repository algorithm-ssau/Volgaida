import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {ContactPageComponent} from "./pages/contact-page/contact-page/contact-page.component";
import {MenuPageComponent} from "./pages/menu-page/menu-page/menu-page.component";
import {HomePageComponent} from "./pages/home-page/home-page/home-page.component";

const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomePageComponent},
  {path: 'contact', component: ContactPageComponent},
  {path: 'menu', component: MenuPageComponent, pathMatch: 'full'},
  {path: '**', redirectTo: '/home'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
