import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BigboardComponent } from './bigboard.component';

describe('BigboardComponent', () => {
  let component: BigboardComponent;
  let fixture: ComponentFixture<BigboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BigboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BigboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
