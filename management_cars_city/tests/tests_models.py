from django.core.exceptions import ValidationError
from django.test import TestCase
from pytest_django.asserts import assertRaisesMessage

from management_cars_city.models import Car, Person


class PersonTest(TestCase):
    def setUp(self):
        self.person = Person(
            2,
            "igor",
            "marques",
            "admin@admin.com",
            "12345678955",
            "11955551234",
            "18 de Abril de 2023 às 12:00",
            "True",
            )

    def test_person_id(self):
        self.assertEqual(self.person.id, 2)

    def test_email_person(self):
        self.assertEqual(self.person.email, "admin@admin.com")

    def test_name_person(self):
        self.assertEqual(self.person.name, "igor")

    def test_lastname_person(self):
        self.assertEqual(self.person.lastname, "marques")

    def test_cpf_person(self):
        self.assertEqual(self.person.cpf, "12345678955")

    def test_created_person(self):
        self.assertTrue(self.person.created, "True")

    def test_owner_car_person(self):
        self.assertTrue(self.person.owner_car, "True")

    def test_format_name_person(self):
        self.assertEqual(self.person.format_name, "Igor")

    def test_format_last_name_person(self):
        self.assertEqual(self.person.format_last_name, "Marques")

    def test_full_name_person(self):
        self.assertEqual(self.person.full_name, "igor marques")

    def test_username_person(self):
        self.assertEqual(self.person.username, "IGOR123")

    def test_format_celular_person(self):
        self.assertEqual(self.person.format_celular, "(11) 95555-1234")

    def test_format_cpf_person(self):
        self.assertEqual(self.person.format_cpf, "123-456-789.55")

    def test_format_status_owner_car_person(self):
        if self.person.format_status_owner_car:
            self.assertTrue(self.person.format_status_owner_car, "Sim")
        else:
            self.assertTrue(self.person.format_status_owner_car, "Não")

    def test_return_str_person(self: Person):
        assert str(self.person) == 'igor'


class CarTest(TestCase):
    def setUp(self):
        self.person_1 = Person.objects.create(name='igor')

        self.car_1 = Car.objects.create(
                                        model='Hatch',
                                        color='Amarelo',
                                        owner=self.person_1)
        self.car_2 = Car.objects.create(
                                        model='Sedã',
                                        color='Azul',
                                        owner=self.person_1)
        self.car_3 = Car.objects.create(
                                        model='Conversivel',
                                        color='Cinza',
                                        owner=self.person_1)
        self.car_4 = Car(
                        model='Hatch',
                        color='Amarelo',
                        owner=self.person_1)

        self.person_2 = Person.objects.create(name='marcia')

        self.car_5 = Car.objects.create(
                                    model='Conversivel',
                                    color='Cinza',
                                    owner=self.person_2)
        self.car_6 = Car.objects.create(
                                    model='Hatch',
                                    color='Amarelo',
                                    owner=self.person_2)
        self.car_7 = Car(
                        model='Hatch',
                        color='Azul',
                        owner=self.person_2)
        self.car_8 = Car(
                        model='Sedã',
                        color='Cinza',
                        owner=self.person_2)

    def test_car_1_id_ok(self):
        self.assertTrue(self.car_1.id, 1)

    def test_car_2_id_ok(self):
        self.assertTrue(self.car_2.id, 2)

    def test_car_1_owner_id_1(self):
        self.assertTrue(self.car_1.owner_id, 1)

    def test_car_3_owner_id_1(self):
        self.assertTrue(self.car_3.owner_id, 1)

    def test_car_5_owner_id_2(self):
        self.assertTrue(self.car_5.owner_id, 2)

    def test_count_car_1_id_in_owner(self):
        self.assertEqual(self.car_1.owner, self.person_1)

    def test_count_car_2_id_in_owner(self):
        self.assertEqual(self.car_2.owner, self.person_1)

    def test_count_car_3_id_in_owner(self):
        self.assertEqual(self.car_3.owner, self.person_1)

    def test_car_3_color_grey(self):
        self.assertEqual(self.car_3.color, 'Cinza')

    def test_car_5_model_conversivel(self):
        self.assertEqual(self.car_5.model, 'Conversivel')

    def test_clean_raises_exceeded_car(self):
        with assertRaisesMessage(
                                ValidationError,
                                'Já possui número máximo de veículos'):
            self.car_4.clean()

    def test_clean_invalid_model(self):
        with assertRaisesMessage(
                                ValidationError,
                                'Este modelo não pode ser selecionado'):
            self.car_7.clean()

    def test_clean_invalid_color(self):
        with assertRaisesMessage(
                ValidationError,
                'Esta cor não pode ser selecionada para este veículo'):
            self.car_8.clean()

    def test_return__str__owner(self: Car):
        assert str(self.car_1) == 'igor'
