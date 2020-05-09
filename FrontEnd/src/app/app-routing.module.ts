import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {WorldstatusComponent} from "./worldstatus/worldstatus.component";
import {CountrystatusComponent} from "./countrystatus/countrystatus.component";
import {CheckComponent} from "./check/check.component";
import {AffectedcountriesComponent} from "./affectedcountries/affectedcountries.component";

const routes: Routes = [{path: '', component: WorldstatusComponent},
  {path:'country',component:CountrystatusComponent},
  {path:'listCountry',component:AffectedcountriesComponent},
  {path:'check',component:CheckComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}

export const routingComponents = [WorldstatusComponent,CountrystatusComponent,AffectedcountriesComponent,CheckComponent]
