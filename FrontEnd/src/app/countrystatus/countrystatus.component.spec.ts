import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CountrystatusComponent } from './countrystatus.component';

describe('CountrystatusComponent', () => {
  let component: CountrystatusComponent;
  let fixture: ComponentFixture<CountrystatusComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CountrystatusComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CountrystatusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
