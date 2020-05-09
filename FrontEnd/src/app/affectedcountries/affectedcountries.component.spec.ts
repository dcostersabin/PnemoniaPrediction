import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AffectedcountriesComponent } from './affectedcountries.component';

describe('AffectedcountriesComponent', () => {
  let component: AffectedcountriesComponent;
  let fixture: ComponentFixture<AffectedcountriesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AffectedcountriesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AffectedcountriesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
