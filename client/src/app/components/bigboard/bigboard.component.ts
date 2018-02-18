import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/switchMap';

import { Player } from '../../entities/player';
import { PlayerService } from '../../services/player.service';

@Component({
  selector: 'app-bigboard',
  templateUrl: './bigboard.component.html',
  styleUrls: [ './bigboard.component.less' ],
  providers: [PlayerService]
})

export class BigboardComponent implements OnInit {
  @Input() selectedPlayer: Player;
  @Output() onSelectedPlayer = new EventEmitter<Player>();

  rankings: Player[];

  constructor(
    private playerService: PlayerService,
    private route: ActivatedRoute
  ) { }

  getPlayers(): void {
    const bb = this;
    this.playerService.getPlayers().then(function(players) {
      bb.rankings = players;
      bb.checkForSinglePlayerUrl();
    });
  }

  checkForSinglePlayerUrl(): void {
    const strRoute = this.route.url['value'][0].path;
    if (strRoute === 'player') {
      const id = this.route.snapshot.paramMap.get('id');
      this.selectedPlayer = this.rankings.filter(function(obj) {
        return obj.id === id;
      })[0];
      this.onSelectedPlayer.emit(this.selectedPlayer);
    }
  }

  onSelect(player: Player, event: Event): void {
    this.onSelectedPlayer.emit(player);
    this.selectedPlayer = player;
    event.preventDefault();
    window.history.pushState(null, player.name, '/player/' + player.id);
  }

  ngOnInit(): void {
    this.getPlayers();
  }
}
