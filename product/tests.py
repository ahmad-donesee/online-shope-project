from django.test import TestCase
from .models import Product,Category
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.


class TestProduct(TestCase):
    def setUp(self):
        self.category=Category.objects.create(
            name="cateone",
            slug="one" 
        )
        
        
        self.product=Product.objects.create(
            name="rrr",price=32,description="tttt",slug="ppp"
        )

    def test_category(self):
        cate=Category.objects.get(id=1)
        self.assertEqual(cate.name,"cateone")
        
    def test_product(self):
        cate=Product.objects.get(id=self.category_id)
        self.assertEqual(cate.name,"rrr")
    