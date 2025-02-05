from product.models import Product
from django.conf import settings
from coupons.models import  Coupons
from decimal import Decimal
class Cart:
    def __init__(self,request):
        self.session=request.session
        self.coupon_id=self.session.get('coupon_id')
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
    
    
    
    def add(self,product,quantity=1,overide_quantity=False):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':product.price}
        if overide_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()
        
    def save(self):
        self.session.modified=True
        self.session[settings.CART_SESSION_ID]=self.cart
        
    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del  self.cart[product_id]
            self.save()
            
    def __iter__(self):
        prodct_ids=self.cart.keys()
        products=Product.objects.filter(id__in=prodct_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        
        for item in cart.values():
            item['total_price']=item['quantity']*item['price']
            yield item
            
    
    
    def __len__(self):
        return sum(item['quantity']for item in self.cart.values())
        
    def get_total_cost(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())
    
    def  clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupons.objects.get(id=self.coupon_id)
            except:
                pass
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount/Decimal(100)*self.get_total_cost())
        else:
            return Decimal(0)
        
    def get_total_price_after_discount(self):
        return (self.get_total_cost()-self.get_discount())














