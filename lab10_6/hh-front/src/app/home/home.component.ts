import { CommonModule, NgFor } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';

import { VacancyComponent } from '../vacancy/vacancy.component';
import { Vacancy } from '../models';
import { AppService } from '../app.service';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule, VacancyComponent, NgFor],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  vacancies !: Vacancy[];
  loaded = false;
  constructor(private route: ActivatedRoute,
    private appService: AppService) {

  }
  ngOnInit(): void {
    this.appService.getTopTenVacancy().subscribe((vacancies) => {
      console.log(vacancies)
      this.vacancies = vacancies;
      this.loaded = true;
    })
  }
}