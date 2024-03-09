from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.forms import Product_quantity_Form
# Create your views here.

def product_view(request):
    category=Category.objects.all()
    product1=Product.objects.all()
    # if category_slug:
    # language=request.LANGUAGE_CODE
    # category=get_object_or_404(Category,translations__language_code=language,translations__slug=category_slug)
    return render(request,"product/product_list.html",{"category":category,"product1":product1})

def item_product_view(request,category_slug=None):
    # item=get_object_or_404(Product,id=id)
    category=Category.objects.all()
    product=Product.objects.all()
    if category_slug:
        language=request.LANGUAGE_CODE
        prod=get_object_or_404(Category,translations__language_code=language,translations__slug=category_slug)
        # prod=get_object_or_404(Category,slug=category_slug)
        product=Product.objects.all().filter(category=prod)
    context={"product":product, "category":category}
    return render(request,'product/product_list.html',context)

def detail_item_view(request,category_slug,id):
    form=Product_quantity_Form()
    language=request.LANGUAGE_CODE
    item=get_object_or_404(Product,translations__language_code=language,translations__slug=category_slug,id=id)
    return render(request,'product/detail_item.html',{'item':item,"form":form}) 
