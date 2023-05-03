from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import CarForm, PersonForm
from .models import Car, Person
from .service import CarService, PersonService


def index_first(request):
    """Página inicial"""
    return render(request, 'index_first.html')


class CreatePerson(CreateView):
    model = Person
    context = {'form': PersonForm()}
    template_name = "register_person.html"
    success_url = reverse_lazy("management_cars_city:index")
    fields = ("name", "lastname", "email", "cpf", "cellphone")


def persons(request):
    """Lista todas as pessoas cadastradas. service.py"""
    list_persons_service = PersonService()
    persons = list_persons_service.list_persons_with_paginated(request)
    context = {'persons': persons}
    return render(request, 'persons.html', context)


def search(request):
    """View para pesquisa de pessoas cadastradas - exclusivo para CPF"""
    termo = request.GET.get('termo')
    persons = Person.objects.order_by('-id').filter(cpf=termo)
    return render(request, 'search.html', {'persons': persons})


def sales_opportunity(request):
    """Listar oportunidades de vendas. service.py"""
    list_all_persons_sales_op = PersonService()
    persons = list_all_persons_sales_op.\
        list_all_persons_with_sales_oportunity(request)
    context = {'persons': persons}
    return render(request, 'sales_opportunity.html', context)


def sales_oportunity_id(request, pk):
    """Listar person_id em oportunidade de venda. service.py"""
    list_id_person_sales_op = PersonService()
    person = list_id_person_sales_op.\
        list_person_id_with_sales_oportunity(request, pk)
    context = {'person': person}
    return render(request, 'sales_opportunity_id.html', context)


class UpdatePerson(UpdateView):
    model = Person
    fields = ["name", "lastname", "email", "cellphone"]
    success_url = reverse_lazy("management_cars_city:index")
    template_name = "update_person.html"


class CreateCar(CreateView):
    model = Car
    context = {'form': CarForm()}
    template_name = "register_car.html"
    success_url = reverse_lazy("management_cars_city:listar_carros_proprietarios")
    fields = ("model", "color", "owner")

    @receiver(post_save, sender=Car)
    def update_owner_car(sender, instance, created, **kwargs):
        """Atualiza status owner_car para True quando criado objeto carro em
        seu person_ID. service.py"""
        if created:
            CarService.receiver_update_owner_car(instance, **kwargs)

    @receiver(pre_delete, sender=Car)
    def update_owner_with_delete_car(sender, instance, **kwargs):
        """Atualiza status owner_car para False quando deletado ultimo carro em
        seu person_ID. service.py"""
        CarService.update_owner_car_delete(instance)


def owners_car(self):
    """Listar todos proprietários de veículos. service.py"""
    list_all_owner_c = CarService()
    cars = list_all_owner_c.list_all_owner_car(self)
    context = {'cars': cars}
    return render(self, 'owner_cars.html', context)


def persons_cars(request, person_id):
    """Listar profile de person_id e detalhes de veículos vinculados
    a este ID"""
    context = CarService.list_profile_person_id_with_car(person_id)
    return render(request, 'person_cars.html', context)


class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('management_cars_city:listar_carros_proprietarios')
    template_name = 'delete_car.html'
