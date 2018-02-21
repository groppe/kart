import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { environment } from '../../environments/environment';
import { Player } from '../entities/player';


@Injectable()
export class PlayerService {

  constructor (private http: Http) { }

  getPlayers(): Promise<Player[]> {
    return this.http.get(environment.WEB_API_ENDPOINT + '/ranking/average')
      .toPromise()
      .then(response => response.json().rankings as Player[])
      .catch(this.handleError);
  }

  getPlayer(id: string): Promise<Player> {
    const url = `${environment.WEB_API_ENDPOINT}/player/${id}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json() as Player)
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error.json()); // demo purposes only
    return Promise.reject(error.message || error);
  }
}
