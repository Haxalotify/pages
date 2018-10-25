#using SimpleTestCase instead of, TestCase, because not using a database
from django.test import SimpleTestCase

# Create your tests here.
class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        #200 is the standard response for a successful HTTP request
        #checking to see if status code for each page = 200
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
