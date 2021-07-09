import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class LolApiService {
  constructor(private http: HttpClient) { }

  coordinates: any;
  deathServiceUrl = 'http://127.0.0.1:5000/deathCoordinates/';

  // requires username(string)
  // returns observable
  getDeaths(username:string) {
    return this.http.get<any>(this.deathServiceUrl+username)
  }
}
