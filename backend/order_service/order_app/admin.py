from django.contrib import admin
from .models import OrderModel, ProductModel, CategoryModel
# Register your models here.

admin.site.register(OrderModel)
admin.site.register(ProductModel)
admin.site.register(CategoryModel)