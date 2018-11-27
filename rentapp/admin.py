from django.contrib import admin

# Register your models here.
from .models import Product, Rent

admin.site.register(Product)
admin.site.register(Rent)