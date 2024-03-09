from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from  .models import Order,OrderItem
from datetime import datetime
# Register your models here.

import csv
from django.http import HttpResponse

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields=['product',]


def export_csv(modeladmin, request, queryset):
    opts= modeladmin.model._meta
    content='attechment; filedname={opts.verbose_name}.csv'
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']=content
    writer=csv.writer(response)
    fields=[field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many ]
    writer.writerow([field.verbose_name for field in fields])
    
    for object in queryset:
        data_list=[]
        for field in fields:
            value=getattr(object,field.name)
            if isinstance(value,datetime):
                value=value.strftime('%Y-%m-%d')
            data_list.append(value)
        writer.writerow(data_list)
    return response

export_csv.short_description="Export to CSV"

def order_detail(obj):
    url=reverse("orders:admin_order_detail",args=[obj.id])
    return mark_safe(f'<a href="{url}">view</a>')

def order_pdf(obj):
    verbose_name="حنمبن"
    lable=mark_safe(f'{verbose_name}-{obj.id}')
    url=reverse("orders:admin_order_pdf",args=[obj.id])
    return (mark_safe(f'<a href="{url}">pdf</a>'))

order_pdf.short_description="Export to pdf"



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name', 'email', 'address', 'city', 'postal_code', 'city',order_detail,order_pdf]
    search_fields=['first_name','last_name', 'email', 'address', 'city', 'postal_code', 'city']
    actions=[export_csv]







