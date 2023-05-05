
import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.serializers import PersonSerializer
from management_cars_city.models import Person


@pytest.fixture
def test_list_person(api_client):
    response = api_client.get('/api/v1/persons/')
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert all('name' in item and 'email' in item for item in response.data)


class ListPersonTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('persons-list')
        self.person_1 = Person.objects.create(
            name='Marcia',
            lastname='Marques',
            email='marcia@gmail.com',
            cellphone='12985210647',
            cpf='45698712354',
        )
        self.person_2 = Person.objects.create(
            name='Aurea',
            lastname='Nascimento',
            email='nascimento@gmail.com',
            cellphone='12985210617',
            cpf='45698412355',
        )
        self.person_3 = Person.objects.create(
            name='Yasmin',
            lastname='Nascimento',
            email='yasmin@gmail.com',
            cellphone='12985210600',
            cpf='45698412300',
        )

    def test_list_persons(self):
        client = APIClient()
        url = reverse('persons-list')

        # Faça a solicitação GET para a URL
        response = client.get(url)

        # Verifique se a resposta é 200 OK
        assert response.status_code == status.HTTP_200_OK

        # Verifique se a resposta contém as informações corretas
        assert len(response.data) == 3
        assert response.data[0]['name'] == 'Yasmin' #Definido retornar por -id
        assert response.data[1]['name'] == 'Aurea'
        assert response.data[2]['name'] == 'Marcia'

    def test_list_persons_2(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        self.assertEqual(len(response.data), 3)

        for person in response.data:
            if person['name'] == 'Marcia':
                self.assertEqual(person['lastname'], 'Marques')
                self.assertEqual(person['email'], 'marcia@gmail.com')
                self.assertEqual(person['cellphone'], '12985210647')
                self.assertEqual(person['cpf'], '45698712354')
            elif person['name'] == 'Aurea':
                self.assertEqual(person['lastname'], 'Nascimento')
                self.assertEqual(person['email'], 'nascimento@gmail.com')
                self.assertEqual(person['cellphone'], '12985210617')
                self.assertEqual(person['cpf'], '45698412355')
            elif person['name'] == 'Yasmin':
                self.assertEqual(person['lastname'], 'Nascimento')
                self.assertEqual(person['email'], 'yasmin@gmail.com')
                self.assertEqual(person['cellphone'], '12985210600')
                self.assertEqual(person['cpf'], '45698412300')

            else:
                self.fail(f'Person {person["name"]} not found')
