from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from management_cars_city.models import Person


class PersonViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.person = Person.objects.create(
                    name='Marcia',
                    lastname='Marques',
                    email='ig@ig.com',
                    cellphone='12985213647',
                    cpf='45698712355',
                )
        self.valid_payload = {'name': 'Aurea'}
        self.invalid_payload = {'email': 'ig-ig.com'}
        self.url = reverse('persons-partial-update-person', kwargs={'pk': self.person.pk})

    def test_partial_update_person_with_valid_payload(self):
        response = self.client.patch(self.url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.person.refresh_from_db()
        self.assertEqual(self.person.name, self.valid_payload['name'])

    def test_partial_update_person_with_invalid_payload(self):
        response = self.client.patch(self.url, data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_person_with_nonexistent_person(self):
        url = reverse('persons-partial-update-person', kwargs={'pk': 999})
        response = self.client.patch(url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
