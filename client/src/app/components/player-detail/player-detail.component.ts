import {
  Component, ElementRef, EventEmitter, Inject, Input, OnChanges, OnInit, Output,
  SimpleChanges
} from '@angular/core';

import { Player } from '../../entities/player';
import { Game } from '../../entities/game';

import { PlayerService } from '../../services/player.service';
import { GameService } from '../../services/game.service';

@Component({
  selector: 'app-player-detail',
  templateUrl: './player-detail.component.html',
  styleUrls: [ './player-detail.component.less' ],
  providers: [
    PlayerService,
    GameService
  ]
})

export class PlayerDetailComponent implements OnInit, OnChanges {
  @Input() player: Player;
  @Input() results: Game[];
  @Input() gameDetail: Game;
  @Output() onCloseDetail: EventEmitter<any> = new EventEmitter();

  private domNode: HTMLElement = null;

  constructor(
    private playerService: PlayerService,
    private gameService: GameService,
    @Inject(ElementRef) elementRef: ElementRef
  ) {
    this.domNode = elementRef.nativeElement;
    this.setTop();
  }

  ngOnInit(): void {
    this.gameService.getGames(this.player.id)
      .then(playerResults => this.results = playerResults);
  }

  ngOnChanges(changes: SimpleChanges) {
    this.setTop();
    this.gameService.getGames(this.player.id)
      .then(playerResults => this.results = playerResults);
  }

  onSelect(gameId: string): void {
    this.gameService.getGame(gameId)
      .then(game => {
        this.gameDetail = game;
        for (const player of this.gameDetail[0].scores) {
          this.playerService.getPlayer(player.player_id)
            .then(playerData => this.gameDetail[0].scores.name = playerData.name)
            .catch(this.handleError);
        }
      } )
      .catch(this.handleError);
  }

  closeOverlay(): void {
    this.gameDetail = null;
  }

  closeDetail(event: Event): void {
    this.onCloseDetail.emit(null);
    event.preventDefault();
    window.history.pushState(null, 'Dashboard', '/dashboard');
  }

  stopPropagation(event: Event) {
    event.stopPropagation();
  }

  private setTop(): void {
    const scrollTop = (window.pageYOffset > 83 || document.documentElement.scrollTop) ?
                        (window.pageYOffset || document.documentElement.scrollTop) :
                        83;
    this.domNode.style.top = scrollTop + 'px';
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // demo purposes only
    return Promise.reject(error.message || error);
  }
}
