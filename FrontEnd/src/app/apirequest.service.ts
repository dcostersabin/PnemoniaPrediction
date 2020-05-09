import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ApirequestService {

  constructor(private http:HttpClient) { }

  getWorldStatus()
  {

    return [];
  }
}
