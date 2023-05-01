
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Car, Person


class PersonService:

    def list_persons_with_paginated(self, request):
        """Listar todas as pessoas cadastradas, com paginação"""
        persons = Person.objects.order_by('-id')
        return self._paginator_person(persons, request)

    def list_all_persons_with_sales_oportunity(self, request):
        """Listar todas as pessoas cadastradas que não possuem veículo"""
        persons = Person.objects.order_by('-id').filter(owner_car=False)
        return self._paginator_person(persons, request)

    def list_person_id_with_sales_oportunity(self, request, pk):
        """Listar person_id que não possui veículo"""
        person = get_object_or_404(Person, id=pk)
        if not person.id:
            raise Http404()
        return person

    def _paginator_person(self, persons, request):
        """Paginação padrão (Person) usada em varias funções do projeto"""
        paginator = Paginator(persons, 5)
        page = request.GET.get('p')
        persons = paginator.get_page(page)
        return persons


class CarService:

    @staticmethod
    def receiver_update_owner_car(instance, **kwargs):
        """Atualizar status owner_car para True"""
        person = instance.owner
        person.owner_car = True
        person.save()

    def list_all_owner_car(self, request):
        """Listar todos os proprietários de veículos"""
        cars = Car.objects.select_related('owner').order_by('-owner_id').all()
        return self._paginator_car(cars, request)

    @staticmethod
    def list_profile_person_id_with_car(person_id):
        """Listar profile_id e cars vinculados ao owner_id"""
        # sourcery skip: inline-immediately-returned-variable
        person = Person.objects.get(id=person_id)
        cars = Car.objects.filter(owner=person_id)
        car_count = person.car_set.count()
        context = {'person': person, 'cars': cars, 'car_count': car_count}
        return context

    def _paginator_car(self, cars, request):
        """Paginação padrão (Car) usada em varias funções do projeto"""
        paginator = Paginator(cars, 5)
        page = request.GET.get('p')
        cars = paginator.get_page(page)
        return cars
