import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { environment } from '../../environments/environment';
import { Player } from '../entities/player';
import { PlayerResult } from '../entities/player-result';


@Injectable()
export class PlayerService {

  constructor (private http: Http) { }

  getPlayers(): Promise<Player[]> {
    return this.http.get(environment.WEB_API_ENDPOINT + '/bigboard')
      .toPromise()
      .then(response => response.json() as Player[])
      .catch(this.handleError);
  }

  getPlayer(id: string): Promise<Player> {
    const url = `${environment.WEB_API_ENDPOINT}/player/${id}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json() as Player)
      .catch(this.handleError);
  }

  getResults(id: string): Promise<PlayerResult[]> {
    const url = `${environment.WEB_API_ENDPOINT}/player/${id}/results`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json() as PlayerResult[])
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // demo purposes only
    return Promise.reject(error.message || error);
  }
}
