from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_view

class HomePageTest(TestCase):

    # def test_bad_math(self):
    #     # this test should fail
    #     self.assertIn(2+2 , 3)

    def test_root_url_to_home_view(self):
        home = resolve('/')
        self.assertEqual(home.func, home_view)

    def test_home_view_returns_correct_html(self):
        request = HttpRequest()
        response = home_view(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'To-Do' , response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
