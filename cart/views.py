from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from orders.models import Order
from product.models import Product
from .forms import Product_quantity_Form
from coupons.forms import CouponForm
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
def cart_add(request,product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    form=Product_quantity_Form(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],overide_quantity=cd['overide'])
        cart.save()
        return redirect("cart:cart_detail")
        
    else:
        form=Product_quantity_Form()
        return render(request,'cart/cart_detail.html',{'cart':cart})
@require_POST
def cart_update(request,product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    form=Product_quantity_Form(request.POST)
    if form.is_valid():
        cart.remove(product)
        cd=form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],overide_quantity=cd['overide'])
        cart.save()
        return redirect("cart:cart_detail")
    else:
        return redirect("cart:cart_detail")




@require_POST
def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")

def cart_detail(request):
    couponform=CouponForm()
    order=Order.objects.all()
    cart=Cart(request)
    form=Product_quantity_Form()
    context={'cart':cart,'form':form,"order":order,"couponform":couponform}
    return render(request,"cart/cart_detail.html",context)
        
    


        