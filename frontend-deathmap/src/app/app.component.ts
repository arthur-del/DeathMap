import { Component } from '@angular/core';
import { LolApiService } from '../app/lol-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private deathService: LolApiService) { }

  coordinates: any;
  title = 'frontend-deathmap';
  username="Sc2troller";

  getDeathMap() {
    this.coordinates = this.deathService.getDeaths()
  }
}
