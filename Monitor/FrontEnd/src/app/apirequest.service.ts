import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {World} from "./world";
import {Observable} from "rxjs";
import {Image} from "./image";
import {CountryStatus} from "./countryStatus";
import {Country} from "./country";

@Injectable({
  providedIn: 'root'
})
export class ApirequestService {

  private worldStatus: string = 'http://127.0.0.1:8000/api/index/';
  // private images: string = 'http://127.0.0.1:8000/api/images/';
  private countryStatus: string = 'http://127.0.0.1:8000/api/country_status/';
  private listCountry: string = 'http://127.0.0.1:8000/api/list_country/';
  private checkXray: string = 'http://127.0.0.1:8000/api/check';


  constructor(private http: HttpClient) {
  }

  // getImages(): Observable<Image[]> {
  //   return this.http.get<Image[]>(`${this.images}`);
  // }

  getWorldStatus(): Observable<World[]> {
    return this.http.get<World[]>(`${this.worldStatus}`);
  }

  getCountryStatus(): Observable<CountryStatus[]> {
    return this.http.get<CountryStatus[]>(`${this.countryStatus}`);
  }

  getCountryList(): Observable<Country[]> {
    return this.http.get<Country[]>(`${this.listCountry}`);
  }



}
