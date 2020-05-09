import {Component, OnInit} from '@angular/core';
import {ApirequestService} from "../apirequest.service";

@Component({
  selector: 'app-worldstatus',
  templateUrl: './worldstatus.component.html',
  styleUrls: ['./worldstatus.component.css']
})
export class WorldstatusComponent implements OnInit {

  public worldStatus = [];

  constructor(private _worldData: ApirequestService) {
  }

  ngOnInit() {
    this.worldStatus = this._worldData.getWorldStatus();
  }

}
