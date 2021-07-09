import { Component } from '@angular/core';
import { LolApiService } from '../app/lol-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(private deathService: LolApiService) {
    this.showMap = false;
    this.username = '';
  }
  mapToPixelRatioX = 512 / 15790;
  mapToPixelRatioY = 512 / 15400;
  showMap: boolean;
  coordinates: any;
  title = 'frontend-deathmap';
  minimap = '../assets/resources/lol_minimap.png';
  username: string;

  getDeathMap() {

    this.coordinates = this.deathService.getDeaths(this.username).subscribe(points => {
      console.log("Please work", points)
      this.coordinates = points;
      this.showMap = true;
    });
  }
  updateUsername(event: Event) {
    this.username = (<HTMLInputElement>event.target).value
  }
}

// - Pass in username data in searchbox
// - Return anyone's death information
// - Return an error from the backend if the username doesn't exist
// - Bonus: - create ngif html that pops if that error occurs