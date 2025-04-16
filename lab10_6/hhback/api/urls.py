from django.contrib import admin
from django.urls import path
from .old_views import *
from .views.company_views import company_list, company_details, company_vacancies
from .views.vacancy_views import VacancyListAPIView, VacancyDetailAPIView, VacancyTopTenAPIView


urlpatterns = [
    path("companies/", company_list),
    path("companies/<int:id>/", company_details),
    path("companies/<int:id>/vacancies/", company_vacancies),
    path("vacancies/", VacancyListAPIView.as_view()),
    path("vacancies/<int:id>/", VacancyDetailAPIView.as_view()),
    path("vacancies/top_ten/", VacancyTopTenAPIView.as_view()),
]
