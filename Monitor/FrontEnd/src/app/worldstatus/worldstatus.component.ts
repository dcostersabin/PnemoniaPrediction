import {Component, OnInit} from '@angular/core';
import {ApirequestService} from "../apirequest.service";
import {Image} from "../image";

@Component({
  selector: 'app-worldstatus',
  templateUrl: './worldstatus.component.html',
  styleUrls: ['./worldstatus.component.css']
})
export class WorldstatusComponent implements OnInit {

  public worldStatus = [];
  // public images = [];


  constructor(private _worldData: ApirequestService, private _img: ApirequestService) {
  }


  ngOnInit() {
    this._worldData.getWorldStatus().subscribe(data => this.worldStatus = data);
    // this._img.getImages().subscribe(data => this.images = data)
  }

}
