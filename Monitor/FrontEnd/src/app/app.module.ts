import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';
import { WorldstatusComponent } from './worldstatus/worldstatus.component';
import { CountrystatusComponent } from './countrystatus/countrystatus.component';
import { AffectedcountriesComponent } from './affectedcountries/affectedcountries.component';
import {ApirequestService} from "./apirequest.service";
import {HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";


@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    WorldstatusComponent,
    CountrystatusComponent,
    AffectedcountriesComponent,


  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ApirequestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
