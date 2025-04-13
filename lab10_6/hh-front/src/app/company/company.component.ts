import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { VacancyComponent } from '../vacancy/vacancy.component';
import { Company, Vacancy } from '../models';
import { AppService } from '../app.service';

@Component({
  selector: 'app-company',
  standalone: true,
  imports: [CommonModule, RouterModule, VacancyComponent],
  templateUrl: './company.component.html',
  styleUrl: './company.component.css'
})
export class CompanyComponent implements OnInit {
  company!: Company;
  vacancies!: Vacancy[];
  constructor(private route: ActivatedRoute,
    private appService: AppService) {

  }
  ngOnInit() {
    this.route.paramMap.subscribe((params) => {
      if (params.get('id')) {
        const companyId = Number(params.get('id'));
            this.appService.getCompany(companyId).subscribe((company) => {
          this.company = company;
        });
        this.appService.getVacancies(companyId).subscribe((vacancies) => {
          this.vacancies = vacancies;
        })
      }
    });
  }

}
