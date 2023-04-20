from http import HTTPStatus

from django.contrib.auth.models import User
from django.http import Http404
from django.test import Client, RequestFactory, TestCase

from management_cars_city.models import Car, Person
from management_cars_city.views import (persons, sales_opportunity,
                                        sales_opportunity_id, search)


class TestViewIndex(TestCase):

    def test_view_index_first(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "index_first.html")


class TestViewSearch(TestCase):
    def setUp(self):
        Person.objects.create(
            name="igor",
            lastname="marques",
            email="admin@admin.com",
            cpf="12345678955",
            cellphone="11955551234",
            created="18 de Abril de 2023 às 12:00",
            owner_car="True",
            )

    def test_view_search_is_ok(self):
        factory = RequestFactory()
        request = factory.get('/search/', {'termo': '12345678955'})
        response = search(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '12345678955')


class TestViewPersons(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.person_2 = Person(
            2,
            "igor",
            "marques",
            "admin@admin.com",
            "12345678955",
            "11955551234",
            "18 de Abril de 2023 às 12:00",
            "False",
            )

    def test_view_persons_with_paginated(self):
        url = '/persons/'
        response = self.client.get(url, {'p': '1'})
        response = persons(response.wsgi_request)
        self.assertEqual(response.status_code, 200)

    def test_view_persons_sales_oportunity(self):
        url = '/oportunity/'
        response = self.client.get(url, {'p': '1'})
        response = persons(response.wsgi_request)
        self.assertEqual(response.status_code, 200)


class TestSalesOpportunityView:
    def setup_method(self):
        self.factory = RequestFactory()
        self.person_2 = Person(
            name="igor",
            lastname="marques",
            email="admin@admin.com",
            cpf="12345678955",
            cellphone="11955551234",
            created="18 de Abril de 2023 às 12:00",
            owner_car="False",
            )

    def test_sales_opportunity_view(self):
        url = '/oportunity/'
        request = self.factory.get(url, {'p': '1'})
        response = sales_opportunity(request)

        assert response.status_code == 200
        assert response.template_name == ['sales_opportunity.html']
        assert response.context_data['persons'].paginator.count == 1
        assert response.context_data['persons'].object_list[0] == self.persons[1]


class TestSalesOpportunityIDView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.person_1 = Person.objects.create(id=1, name='igor')
        self.person_2 = Person.objects.create(id=2, name='clara')

    def test_view_sales_oportunity_id_valid_return_200(self):
        request = self.factory.get(f'/{self.person_1.pk}')
        response = sales_opportunity_id(request, self.person_1.pk)
        self.assertEqual(response.status_code, 200)

    def test_view_sales_oportunity_id_invalid_return_404(self):
        request = self.factory.get(f'/{self.person_1.pk}')
        with self.assertRaises(Http404):
            sales_opportunity_id(request, 951)


class TestOwnersCar(TestCase):
    def setUp(self):
        self.client = Client()
        self.person_1 = Person.objects.create(name='igor')

        self.car_1 = Car.objects.create(
                                        model='Hatch',
                                        color='Amarelo',
                                        owner=self.person_1)
        self.car_2 = Car.objects.create(
                                        model='Sedã',
                                        color='Azul',
                                        owner=self.person_1)

    def test_view_owner_cars(self):
        response = self.client.get('/owner')
        self.assertEqual(response.status_code, 200)


class TestPersonCar(TestCase):
    def setUp(self):
        self.client = Client()
        self.person = Person.objects.create(name='igor')
        self.car1 = Car.objects.create(make='Toyota', model='Camry', owner=self.person)
        self.car2 = Car.objects.create(make='Honda', model='Civic', owner=self.person)

    def test_persons_cars(self):
        response = self.client.get(f'/persons_cars/{self.person.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person_cars.html')
        self.assertEqual(response.context['person'], self.person)
        self.assertQuerysetEqual(response.context['cars'], [repr(self.car1), repr(self.car2)])
        self.assertEqual(response.context['car_count'], 2)
