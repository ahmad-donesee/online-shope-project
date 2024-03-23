from django.shortcuts import render,get_object_or_404
from orders.models import Order
from product.models import Product
from django.conf import settings
from django.forms.models import model_to_dict
import requests
import json
# from zeep import Client

#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/verify/'

# /zarinpal
def product_to_dict(product):
                return {
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                }
def send_request(request,order_id=None):
    # if order_id:
    product=Product.objects.get(id=order_id)
    serialized_product = json.dumps(product(product))
    order_id=request.session['order_id']
    order=get_object_or_404(Order,id=order_id)
    total_cost=order.get_total_cost()
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount":amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data,
    headers = {'content-type':'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, headers=headers,data=data, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response
    
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response