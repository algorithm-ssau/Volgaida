import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AboutPageComponent} from "./pages/about-page/about-page.component";
import {MenuPageComponent} from "./pages/menu-page/menu-page.component";
import {HomePageComponent} from "./pages/home-page/home-page.component";

const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomePageComponent},
  {path: 'about', component: AboutPageComponent},
  {path: 'menu', component: MenuPageComponent, pathMatch: 'full'},
  {path: '**', redirectTo: '/home'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
