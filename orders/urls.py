from django.urls import path
from .views import order_list,admin_order_detail,admin_order_pdf
app_name="orders"

urlpatterns = [
    path('',order_list,name="order_list"),
    path('admin/order/<int:order__id>/',admin_order_detail,name="admin_order_detail"),
    path('admin/order/<int:order__id>/pdf',admin_order_pdf,name="admin_order_pdf"),
]