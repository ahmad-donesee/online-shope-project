from django.shortcuts import render,redirect
from .forms import  CouponForm
from django.utils import timezone
from . models import Coupons
from django.views.decorators.http import  require_POST
# Create your views here.

@require_POST
def coupon_view(request):
    time=timezone.now()
    form=CouponForm(request.POST)
    if form.is_valid():
        code=form.cleaned_data['code']
        try:
            coupon=Coupons.objects.get(code__iexact=code,valid_from__lte=time,valid_to__gte=time,active=True)
            request.session['coupon_id']=coupon.id
        except:
            request.session['coupon_id']=None
    return redirect("cart:cart_detail")