import { Component, HostBinding } from '@angular/core';

import { Player } from '../../entities/player';


@Component({
  selector: 'app-dashbaord',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.less']
})

export class DashboardComponent {
  selectedPlayer: Player;

  constructor() {}

  @HostBinding('class.has-details') hasDetails = false;

  onSelectedPlayer(player: Player) {
    this.selectedPlayer = player;
    this.hasDetails = true;
  }

  closeDetails(event: Event): void {
    this.selectedPlayer = null;
    this.hasDetails = false;
  }
}
