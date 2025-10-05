from django.contrib import admin

# Register your models here.
from .models import ProductsModel
admin.site.register(ProductsModel)