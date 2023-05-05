from http import HTTPStatus

import pytest
from django.test import TestCase
from django.urls import reverse

from management_cars_city.models import Car, Person
from management_cars_city.service import CarService


class CarServiceTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            name='igor',
            lastname='marques',
            email='igor@igor.com',
            cpf='12345678955',
            cellphone='11955551234',
        )
        self.car = Car.objects.create(
            owner=self.person,
            model='Hatch',
            color='Amarelo',
        )

    def test_update_owner_car_delete(self):
        CarService.update_owner_car_delete(self.car)
        self.person.refresh_from_db()
        self.assertFalse(self.person.owner_car)

    def test_update_delete_car(self):
        CarService.update_delete_car(self.car)
        self.person.refresh_from_db()
        self.assertFalse(self.person.owner_car)
        self.assertIsNone(Car.objects.filter(pk=self.car.pk).first())


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
