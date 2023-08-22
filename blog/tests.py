from urllib import response
from django.test import TestCase

# Create your tests here.


class TestPage(TestCase):

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
