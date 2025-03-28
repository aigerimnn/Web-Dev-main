from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('companies', views.profile, name='profile'),
    path('companies/<int:id>', views.company, name='company'),
    path('companies/<int:id>/vacancies', views.companyVacancies, name='companyVacancies'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('vacancies/<int:id>', views.vacancyId, name='vacancyId'),
    path('vacancies/top_ten', views.top_ten, name='top_ten'),
]