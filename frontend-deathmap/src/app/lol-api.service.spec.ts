import { TestBed } from '@angular/core/testing';

import { LolApiService } from './lol-api.service';

describe('LolApiService', () => {
  let service: LolApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LolApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
