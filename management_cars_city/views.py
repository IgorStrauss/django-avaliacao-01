#from django.http import HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CarForm, PersonForm
from .models import Car, Person


def index_first(request):
    return render(request, 'index_first.html')


class CreatePerson(CreateView):
    model = Person
    context = {'form': PersonForm()}
    template_name = "register_person.html"
    success_url = reverse_lazy("management_cars_city:listar_pessoas")
    fields = ("name", "lastname", "email", "cpf", "cellphone")


def persons(self):
    persons = Person.objects.order_by('-id')
    return render(self, 'persons.html', {'persons': persons})


def sales_opportunity(request):
    persons = Person.objects.order_by('-id').filter(owner_car=False)
    return render(request, 'sales_opportunity.html', {'persons': persons})


def sales_opportunity_id(request, pk):
    person = Person.objects.get(id=pk)
    return render(request, 'sales_opportunity_id.html', {'person': person})


class CreateCar(CreateView):
    model = Car
    context = {'form': CarForm()}
    template_name = "register_car.html"
    success_url = reverse_lazy("management_cars_city:listar_carros_proprietarios")
    fields = ("model", "color", "owner")

    @receiver(post_save, sender=Car)
    def update_owner_car(sender, instance, created, **kwargs):
        if created:
            person = instance.owner
            person.owner_car = True
            person.save()


def owners_car(request):
    cars = Car.objects.select_related('owner').all()
    return render(request, 'owner_cars.html',
                  {'cars': cars})


def persons_cars(request, person_id):
    person = Person.objects.get(id=person_id)
    car_count = person.car_set.count()
    context = {'person': person, 'car_count': car_count}
    return render(request, 'person_cars.html', context)
