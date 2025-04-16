import { Component, Input } from '@angular/core';
;
import { CommonModule } from '@angular/common';
import { Vacancy } from '../models';

@Component({
  selector: 'app-vacancy',
  standalone: true,
  imports: [VacancyComponent, CommonModule],
  templateUrl: './vacancy.component.html',
  styleUrl: './vacancy.component.css'
})
export class VacancyComponent {
  @Input() vacancy!: Vacancy;

}