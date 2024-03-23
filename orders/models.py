from django.db import models
from django.utils import timezone
from cart.cart import Cart
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from product.models import Product
# Create your models here.

class Order(models.Model):
    username =models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)  # blank=True means that the
    first_name=models.CharField(_("name"),max_length=20)
    last_name=models.CharField(_("family"),max_length=20)
    address=models.CharField(_("address"),max_length=100,null=True)
    phone=models.IntegerField(_("phone"),)
    email=models.EmailField(_("email"),max_length=254)
    postal_code=models.CharField(_("postal_code"),max_length=25)
    city=models.CharField(_("city"),max_length=20)
    created_at=models.DateTimeField(_("created"),auto_now_add=True)
    update_at=models.DateTimeField(_("update"),auto_now=True)
    
    def __str__(self):
        return f"Order by {self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ['-created_at']
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE ,related_name='items')
    product=models.ForeignKey(Product,related_name="order_item",on_delete=models.CASCADE)
    price=models.PositiveBigIntegerField()
    quantity=models.PositiveIntegerField()
    
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price*self.quantity
    
    