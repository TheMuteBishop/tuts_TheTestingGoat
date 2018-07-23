from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_view
from .models import Item
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
        expected_html_file = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected_html_file)

    def test_home_view_can_save_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'An new list item'
        
        response = home_view(request)

        self.assertIn('An new list item', response.content.decode())

        expected_html = render_to_string('lists/home.html', {'item_text' : 'An new list item'})
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):

    def test_saving_and_retriving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text , 'The first (ever) item')
        self.assertEqual(second_saved_item.text , 'Item the second')
