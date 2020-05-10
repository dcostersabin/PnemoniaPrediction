import {Component, OnInit} from '@angular/core';
import {ApirequestService} from "../apirequest.service";

@Component({
  selector: 'app-countrystatus',
  templateUrl: './countrystatus.component.html',
  styleUrls: ['./countrystatus.component.css']
})
export class CountrystatusComponent implements OnInit {

  public countryStatus = []

  constructor(private _countryStatus: ApirequestService) {
  }

  ngOnInit(): void {
    this._countryStatus.getCountryStatus().subscribe(data => this.countryStatus = data);
  }

}
