from django.test import TestCase


class UrlsTestCase(TestCase):
    def test_url_index_return_ok(self):
        url = "/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, "Página inicial")
