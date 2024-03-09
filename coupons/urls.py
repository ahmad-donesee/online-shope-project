from django.urls import path
from .views import coupon_view
app_name="coupons"

urlpatterns = [
    path("",coupon_view,name="coupon_view"),
]
