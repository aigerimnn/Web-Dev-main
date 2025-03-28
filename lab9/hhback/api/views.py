from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.core.serializers import serialize
from api.models import Company, Vacancy


# Create your views here.
def members(request):
  template = loader.get_template('1.html')
  return HttpResponse(template.render())

def company(request, id):
  company = get_object_or_404(Company, id=id)
  data = {'product': model_to_dict(company)}
  return JsonResponse(data)


def profile(request):
  companies = Company.objects.all()
  data = {'companies': list(companies.values())}
  return JsonResponse(data)


def vacancies(request):
  vacancies = Vacancy.objects.all()
  vacancies_json = serialize('json', vacancies)
  return HttpResponse(vacancies_json, content_type='application/json')

def vacancyId(request, pk):
  try:
    vacancy = Vacancy.objects.get(pk=pk)
  except:
    raise Http404("This vacancy does not exist")
  return JsonResponse(vacancy.to_json(), safe=False)

def companyVacancies(request, id):
  c = Company.objects.get(id=id)
  vacancies = Vacancy.objects.filter(company=c)
  vacancies_json = [v.to_json() for v in vacancies]
  return JsonResponse(vacancies_json, safe=False)

def top_ten(request):
  vacancies = Vacancy.objects.all().order_by('-salary')[:10]
  vacancies_json = [v.to_json() for v in vacancies]
  return JsonResponse(vacancies_json, safe=False)