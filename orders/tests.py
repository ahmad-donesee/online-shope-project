from django.test import TestCase,SimpleTestCase
from . models import Order,OrderItem
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your tests here.

class SimpleTest(TestCase):
    def test_order_list_pages(self):
        response=self.client.get('/en/orders/')
        self.assertEqual(response.status_code,200)
    def test_orders_successed_page(self):
        response=self.client.get('/en/orders/?')
        self.assertEqual(response.status_code,200)



        
        
        
