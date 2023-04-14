#from django.http import HttpResponse
from django.shortcuts import render

from .models import Car, Person


def index_first(request):
    return render(request, 'index_first.html')


def persons(request):
    persons = Person.objects.order_by('-id').filter(owner_car=True)
    return render(request, 'persons.html', {'persons': persons})


def sales_opportunity(request):
    persons = Person.objects.order_by('-id').filter(owner_car=False)
    return render(request, 'sales_opportunity.html', {'persons': persons})


def owner_car(request):
    cars = Car.objects.all()
    return render(request, 'owner_cars.html',
                  {'cars': cars})
