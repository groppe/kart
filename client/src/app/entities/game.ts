import { GameScore } from './game-score';

export class Game {
  _id: string;
  datetime: Date;
  games: Number;
  scores: GameScore[];
}
