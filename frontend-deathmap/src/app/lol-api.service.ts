import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class LolApiService {



  constructor(private http: HttpClient) { }

  coordinates: any;
  deathServiceUrl = 'http://127.0.0.1:5000/deathCoordinates/sc2troller';

  // requires username(string)
  // returns observable
  getDeaths() {
    console.log("in death service: ", this.http.get<any>(this.deathServiceUrl)
      .subscribe(data => {
        this.coordinates = data
      }))
      return this.coordinates
  }
}
