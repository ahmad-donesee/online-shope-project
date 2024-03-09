from django.urls import path
from . views import item_product_view,detail_item_view,product_view
app_name="product"

urlpatterns = [
    path("",product_view, name='product_view'),
    path("<slug:category_slug>/",item_product_view,name="item_product_view"),
    #  path("<int:category__id>/",item_product_view,name="item_product_view"),
    path("<slug:category_slug>/<int:id>/",detail_item_view,name="detail_item_view")
]

