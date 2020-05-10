import {Component, OnInit} from '@angular/core';
import {ApirequestService} from "../apirequest.service";
import {Country} from "../country";

@Component({
  selector: 'app-affectedcountries',
  templateUrl: './affectedcountries.component.html',
  styleUrls: ['./affectedcountries.component.css']
})
export class AffectedcountriesComponent implements OnInit {

  public listCountry = [];

  constructor(private _listCountry: ApirequestService) {
  }

  ngOnInit(): void {
    this._listCountry.getCountryList().subscribe(data => this.listCountry = data);
  }

}
