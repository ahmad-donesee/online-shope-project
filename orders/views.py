from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.http import  HttpResponse
import os
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

def order_list(request):
    cart=Cart(request)
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            cart.clear()
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