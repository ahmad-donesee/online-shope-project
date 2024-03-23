from django.shortcuts import render,redirect,get_object_or_404
from product.models import Product
from django.conf import settings
from django.http import  HttpResponse
from django.urls import reverse
from django.core import serializers
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder

import os
import json
import weasyprint
# from weasyprint import HTML,CSS
from django.template.loader import render_to_string
from django.urls import reverse
# from .tasks import  order_message
from .models import Order,OrderItem
from .forms import  OrderForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def product_to_dict(product):
                return {
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                }
#  product=json.dumps(item['product'],cls=DjangoJSONEncoder)
                # product = serializers.serialize("json", [item['product']])
                # product=json.dumps(model_to_dict(item['product']))
                # product = serializers.serialize("json", [item['product'], ])
                # product=json.dumps(model_to_dict(item['product']),cls=DjangoJSONEncoder)
                # OrderItem.objects.create(product,order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
def order_list(request):
    cart=Cart(request)
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save()
            order.save()
            for item in cart:
                # product = serializers.serialize("json", [item['product']])
                # OrderItem.objects.create(order=order,quantity=item['quantity'],product=json.loads(product))
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity']) #,product=json.loads(product)) 
            # cart.clear()
            # request.session['order_id']=order.id
            # return redirect(reverse("zarinpal:request"))
            return render(request,'orders/order_successed.html',{'form':form,"order":order})         
    else:
        form=OrderForm()
        return render(request,'orders/order_list.html',{'form':form})


@staff_member_required
def admin_order_detail(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request,"admin/orders/order/detail.html",{"order":order})

@staff_member_required
def admin_order_pdf(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    html=render_to_string("orders/order/orderpdf.html",{"order":order})
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] =f"filename=order_{order.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(response,stylsheets=[weasyprint.CSS(settings.STATIC_ROOT+"css/pdf.css")])
    return response