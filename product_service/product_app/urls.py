from django.urls import path
from .views import CategoryView, ProductView, CategoryViewGet, ProductViewGet
urlpatterns = [
    path('create_category/', CategoryView.as_view(), name='create_category_api'),
    path('create_product/', ProductView.as_view(), name='create_product_api'),
    path('categories/', CategoryViewGet.as_view(), name='categories_api'),
    path('products/', ProductViewGet.as_view(), name='products_api'),
]