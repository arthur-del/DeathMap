import { Component } from '@angular/core';
import { LolApiService } from '../app/lol-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(private deathService: LolApiService) {
    this.showMap = false
  }
  mapToPixelRatioX = 512/15790;
  mapToPixelRatioY = 512/15400;
  showMap: boolean;
  coordinates: any;
  title = 'frontend-deathmap';
  username = "Sc2troller";
  minimap = '../assets/resources/lol_minimap.png';

   getDeathMap() {
    this.coordinates = this.deathService.getDeaths().subscribe(points => {
      console.log("Please work",points)
      this.coordinates = points;
      this.showMap = true;
    });
    
    console.log("Sheeesh what's this?", this.coordinates)
  }
}
