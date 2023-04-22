from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import CarForm, PersonForm
from .models import Car, Person


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
    """Lista todas as pessoas cadastradas, independente de possuir veículos"""
    persons = Person.objects.order_by('-id')
    paginator = Paginator(persons, 7)

    page = request.GET.get('p')
    persons = paginator.get_page(page)
    context = {'persons': persons}

    return render(request, 'persons.html', context)


def search(request):
    """View para pesquisa de pessoas cadastradas - exclusivo para CPF"""
    termo = request.GET.get('termo')
    persons = Person.objects.order_by('-id').filter(cpf=termo)
    return render(request, 'search.html', {'persons': persons})


def sales_opportunity(request):
    """Renderiza lista de todas as pessoas que ainda não possuem veículo"""
    persons = Person.objects.order_by('-id').filter(owner_car=False)
    paginator = Paginator(persons, 7)
    page = request.GET.get('p')
    persons = paginator.get_page(page)
    context = {'persons': persons}
    return render(request, 'sales_opportunity.html', context)


def sales_oportunity_id(request, pk):
    """Renderiza pessoa cadastrada que ainda não possui veículo"""
    person = get_object_or_404(Person, id=pk)
    context = {'person': person}
    if not person.id:
        raise Http404()

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
        if created:
            person = instance.owner
            person.owner_car = True
            person.save()


def owners_car(request):
    """Renderiza todos os proprietários de veículos"""
    cars = Car.objects.select_related('owner').order_by('-owner_id').all()
    paginator = Paginator(cars, 7)
    context = {'cars': cars}
    page = request.GET.get('p')
    cars = paginator.get_page(page)

    return render(request, 'owner_cars.html',
                  context)


def persons_cars(request, person_id):
    """Renderiza proprietário de veículo(s) com informações pessoais e dados do(s) veículo(s)"""
    person = Person.objects.get(id=person_id)
    cars = Car.objects.filter(owner=person_id)
    car_count = person.car_set.count()
    context = {'person': person, 'cars': cars, 'car_count': car_count}
    return render(request, 'person_cars.html', context)


class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('management_cars_city:listar_carros_proprietarios')
    template_name = 'delete_car.html'
