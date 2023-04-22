from django.test import TestCase
from django.urls import reverse


class UrlsTestApp(TestCase):

    def test_url_home_is_correct(self):
        index_url = reverse('management_cars_city:index')
        self.assertEqual(index_url, '/')

    def test_url_persons_is_correct(self):
        persons_url = reverse('management_cars_city:listar_pessoas')
        self.assertEqual(persons_url, '/persons')

    def test_url_oportunity_is_correct(self):
        oportunity_url = reverse('management_cars_city:oportunidade_venda')
        self.assertEqual(oportunity_url, '/oportunity')

    def test_url_owner_is_correct(self):
        owner_url = reverse('management_cars_city:listar_carros_proprietarios')
        self.assertEqual(owner_url, '/owner')

    def test_url_register_car_is_correct(self):
        register_car_url = reverse('management_cars_city:register_car')
        self.assertEqual(register_car_url, '/register-car')

    def test_url_create_person_is_correct(self):
        create_person_url = reverse('management_cars_city:create_person')
        self.assertEqual(create_person_url, '/create-person')

    def test_url_sales_opportunity_id_is_correct(self):
        sales_opportunity_id_url = reverse(
            'management_cars_city:sales', args=[2])
        self.assertEqual(sales_opportunity_id_url, '/2/')

    def test_url_profile_car_owner_id_is_correct(self):
        url_profile_car_owner_id_url = reverse(
            'management_cars_city:contagem', args=[2])
        self.assertEqual(url_profile_car_owner_id_url, '/persons-cars/2/')

    def test_url_update_person_id_is_correct(self):
        url_update_person_id_url = reverse(
            'management_cars_city:update_person', args=[2])
        self.assertEqual(url_update_person_id_url, '/update/2/')

    def test_url_delete_car_id_is_correct(self):
        url_delete_car_id_url = reverse('management_cars_city:delete_car',
                                        args=[2])
        self.assertEqual(url_delete_car_id_url, '/delete-car/2/')

    def test_url_search_return_is_ok(self):
        url_search_return_termo = reverse('management_cars_city:pesquisar')
        self.assertEqual(url_search_return_termo, '/search/')


