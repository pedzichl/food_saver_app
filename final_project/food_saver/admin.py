from django.contrib import admin
from .models import Product
# Register your models here.

class AddProduct(admin.ModelAdmin):
    fields = ['name', 'expiration_date', 'quantity', 'unit', 'type']

admin.site.register(Product, AddProduct)

