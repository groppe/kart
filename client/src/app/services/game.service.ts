import { Injectable} from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { environment } from '../../environments/environment';
import { Game } from '../entities/game';


@Injectable()
export class GameService {

  constructor (private http: Http) { }

  getGame(id: string): Promise<Game> {
    const url = `${environment.WEB_API_ENDPOINT}/game/${id}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json() as Game)
      .catch(this.handleError);
  }

  getGames(id: string): Promise<Game[]> {
    const url = `${environment.WEB_API_ENDPOINT}/game?player_id=${id}&size=30`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json().games as Game[])
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // demo purposes only
    return Promise.reject(error.message || error);
  }
}
