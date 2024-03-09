from django.contrib import admin
from .models import Category , Product
from parler.admin import  TranslatableAdmin
# Register your Admins here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name' , 'slug')
    def get_prepopulated_fields(self, request, obj=None):
        return { "slug": ("name",)}
    # prepopulated_fields = {"slug": ("name",)}
    
@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'price','available',]
    list_filter = ['available']
    search_fields = ['name']
    def get_prepopulated_fields(self, request, obj=None):
        return { "slug": ("name",)}
    # prepopulated_fields = {"slug": ("name",)}