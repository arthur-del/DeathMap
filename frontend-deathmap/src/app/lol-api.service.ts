import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



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
    return this.http.get<any>(this.deathServiceUrl)
  }
}
