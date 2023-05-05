import pytest
from django.test import TestCase
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient

from api import serializers
from api.serializers import CarSerializer, PersonCarSerializer
from management_cars_city.models import Car, Person


class CarSerializerTest(TestCase):
    class Meta:
        model = Car
        fields = '__all__'


class CarSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.person = Person.objects.create(name='igor',
                                            lastname='marques',
                                            cpf='12345678901',
                                            email='igor@igor.com',
                                            cellphone='12345678901')

        self.owner = {'id': self.person.id, 'car_set.count()' : 0}


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def person():
    return Person.objects.create(name='igor',
                                 lastname='marques',
                                 cpf='12345678901',
                                 email='igor@igor.com',
                                 cellphone='12345678901')


@pytest.mark.django_db
def test_car_with_same_model(client, person):
    Car.objects.create(owner=person, model='Hatch', color='Amarelo')
    Car.objects.create(owner=person, model='Sedã', color='Azul')

    invalid_data = {'owner': person.id, 'model': 'Hatch', 'color': 'Azul'}
    response = client.post('http://localhost:8000/api/v1/cars/create/',
                           invalid_data)
    expected_errors = {'non_field_errors': [
        'Este modelo não pode ser selecionado']}
    assert response.status_code == 400
    assert response.json() == expected_errors


@pytest.mark.django_db
def test_car_with_same_color(client, person):
    Car.objects.create(owner=person, model='Hatch', color='Amarelo')
    Car.objects.create(owner=person, model='Sedã', color='Azul')

    invalid_data = {'owner': person.id, 'model': 'Conversivel',
                    'color': 'Azul'}
    response = client.post('http://localhost:8000/api/v1/cars/create/',
                           invalid_data)
    expected_errors = {'non_field_errors': [
        'Esta cor não pode ser selecionada']}
    assert response.status_code == 400
    assert response.json() == expected_errors


@pytest.mark.django_db
def test_car_max_quantity(client, person):
    Car.objects.create(owner=person, model='Hatch', color='Amarelo')
    Car.objects.create(owner=person, model='Sedã', color='Azul')
    Car.objects.create(owner=person, model='Conversivel', color='Cinza')

    invalid_data = {'owner': person.id, 'model': 'Conversivel',
                    'color': 'Azul'}
    response = client.post('http://localhost:8000/api/v1/cars/create/',
                           invalid_data)
    expected_errors = {'non_field_errors': [
        'Já possui número máximo de veículos']}
    assert response.status_code == 400
    assert response.json() == expected_errors


# @pytest.fixture
# def test_validate_return_data(person):
#     data = {'owner': person, 'model': 'Hatch', 'color': 'Amarelo'}
#     serializer = CarSerializer(data=data)
#     assert serializer.is_valid() == True
#     assert serializer.validated_data == data

@pytest.mark.django_db
def test_get_cars(client, person):
    car_1 = Car.objects.create(owner=person, model='Hatch', color='Amarelo')
    car_2 = Car.objects.create(owner=person, model='Sedã', color='Azul')
    car_3 = Car.objects.create(owner=person, model='Conversivel', color='Cinza')

    response = client.get(f'http://localhost:8000/api/v1/person_car/{person.id}/')
    assert response.status_code == 200

    expected_data = {
        'id': person.id,
        'name': person.name,
        'lastname': person.lastname,
        'email': person.email,
        'cpf': person.cpf,
        'cellphone': person.cellphone,
        'full_name': person.full_name,
        'cars': [
            {
                'id': car_1.id,
                'model': 'Hatch',
                'color': 'Amarelo',
                'owner': person.id,
            },
            {
                'id': car_2.id,
                'model': 'Sedã',
                'color': 'Azul',
                'owner': person.id,
            },
            {
                'id': car_3.id,
                'model': 'Conversivel',
                'color': 'Cinza',
                'owner': person.id,
            },
        ],
    }
    assert response.data == expected_data


@pytest.mark.django_db
def test_get_cars_return(person):
    Car.objects.create(owner=person, model='Hatch', color='Amarelo')
    Car.objects.create(owner=person, model='Sedã', color='Azul')
    Car.objects.create(owner=person, model='Conversivel', color='Cinza')

    serializer = PersonCarSerializer()
    expected_data = serializer.get_cars(person)

    assert len(expected_data) == 3

    assert expected_data[0]['model'] == 'Hatch'
    assert expected_data[0]['color'] == 'Amarelo'

    assert expected_data[1]['model'] == 'Sedã'
    assert expected_data[1]['color'] == 'Azul'

    assert expected_data[2]['model'] == 'Conversivel'
    assert expected_data[2]['color'] == 'Cinza'
""""""
@pytest.mark.django_db
def test_validate_return_data(person):
    serializer = CarSerializer()

    # Test case for valid input
    data = {'owner': person, 'model': 'Hatch', 'color': 'Amarelo'}
    result = serializer.validate(data)
    assert result == data

    def test_car_limit_exceeded(test_validate_return_data):
        # Test case where owner already has 3 cars
        Car.objects.create(owner=person, model='Hatch', color='Amarelo')
        Car.objects.create(owner=person, model='Sedã', color='Azul')
        Car.objects.create(owner=person, model='Conversivel', color='Cinza')
        data = {'owner': person, 'model': 'Hatch', 'color': 'Azul'}
        with pytest.raises(ValidationError, match='Já possui número máximo de veículos'):
            serializer.validate(data)

    def test_model_exists(test_validate_return_data):
        # Test case where the model has already been selected
        Car.objects.create(owner=person, model='Sedã', color='Cinza')
        data = {'owner': person, 'model': 'Sedã', 'color': 'Amarelo'}
        with pytest.raises(ValidationError, match='Este modelo não pode ser selecionado'):
            serializer.validate(data)

    def test_color_exists(test_validate_return_data):
        # Test case where the color has already been selected
        Car.objects.create(owner=person, model='Conversivel', color='Amarelo')
        data = {'owner': person, 'model': 'Sedã', 'color': 'Amarelo'}
        with pytest.raises(ValidationError, match='Esta cor não pode ser selecionada'):
            serializer.validate(data)
