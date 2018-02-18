import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule} from '@angular/forms';
import { HttpModule } from '@angular/http';


import { AppComponent } from './app.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { PlayerDetailComponent} from './components/player-detail/player-detail.component';
import { BigboardComponent} from './components/bigboard/bigboard.component';

import { PlayerService } from './services/player.service';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  imports:      [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  declarations: [
    AppComponent,
    DashboardComponent,
    PlayerDetailComponent,
    BigboardComponent,
  ],
  providers: [ PlayerService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
