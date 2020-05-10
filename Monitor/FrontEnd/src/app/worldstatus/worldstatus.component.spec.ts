import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorldstatusComponent } from './worldstatus.component';

describe('WorldstatusComponent', () => {
  let component: WorldstatusComponent;
  let fixture: ComponentFixture<WorldstatusComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorldstatusComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorldstatusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
