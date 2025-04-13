from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def get_companies(request):
    companies = Company.objects.all()
    companies_json = [comp.to_json() for comp in companies]
    return JsonResponse(companies_json, safe=False)


def get_company_by_id(request, id):
    companies = Company.objects.get(id=id)
    companies_json = companies.to_json()
    return JsonResponse(companies_json, safe=False)


def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vac.to_json() for vac in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def get_vacancies_by_id(request, id):
    vacancies = Vacancy.objects.get(id=id)
    vacancies_json = vacancies.to_json()
    return JsonResponse(vacancies_json, safe=False)


def get_vacancy_by_company(request, id):
    vacancies = Vacancy.objects.filter(company=id)
    vacancies_json = [vac.to_json() for vac in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vac.to_json() for vac in vacancies]
    return JsonResponse(vacancies_json, safe=False)


