from http import HTTPStatus

import pytest
from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from management_cars_city.models import Car, Person
from management_cars_city.views import persons, search


class TestViewIndex(TestCase):

    def test_view_index_first(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "index_first.html")


class TestViewSearch(TestCase):
    def setUp(self):
        self.person_1 = Person.objects.create(
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
        self.person_1 = Person.objects.create(
            name="igor",
            lastname="marques",
            email="admin@admin.com",
            cpf="12345678955",
            cellphone="11955551234",
            created="18 de Abril de 2023 às 12:00",
            owner_car="True",
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


class TestSalesOpportunity(TestCase):
    def setUp(self):
        self.client = Client()
        self.person_1 = Person.objects.create(
            id=1,
            name="igor",
            lastname="marques",
            email="admin@admin.com",
            cpf="12345678955",
            cellphone="11955551234",
            created="18 de Abril de 2023 às 12:00",
            owner_car="False",
            )

    def test_view_sales_oportunity(self):
        response = self.client.get('/oportunity')
        self.assertEqual(response.status_code, 200)


class SalesOportunityID(TestCase):
    @pytest.mark.django_db(transaction=True)
    def test_view_sales_oportunity_id(self):
        person_1 = Person.objects.create(
            pk=1,
            name="igor",
            lastname="marques",
            email="admin@admin.com",
            cpf="12345678955",
            cellphone="11955551234",
            created="18 de Abril de 2023 às 12:00",
            owner_car="False",
            )
        response = self.client.get(reverse('management_cars_city:sales',
                                           args=[999]))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse('management_cars_city:sales',
                                           args=[person_1.id]))
        self.assertEqual(response.status_code, HTTPStatus.OK)


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


class TestPersonsCars(TestCase):
    @pytest.mark.django_db(transaction=True)
    def test_view_person_car(self):
        person_1 = Person.objects.create(
            pk=1,
            name="igor",
            lastname="marques",
            email="admin@admin.com",
            cpf="12345678955",
            cellphone="11955551234",
            created="18 de Abril de 2023 às 12:00",
            owner_car="True",
            )
        self.car_1 = Car.objects.create(
                                        model='Hatch',
                                        color='Amarelo',
                                        owner=person_1)
        self.car_2 = Car.objects.create(
                                        model='Sedã',
                                        color='Azul',
                                        owner=person_1)
        response = self.client.get(reverse('management_cars_city:contagem',
                                           args=[person_1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['car_count'], 2)
        self.assertEqual(list(response.context['cars']),
                         [self.car_1, self.car_2])
