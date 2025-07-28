from django.urls import path
from .views import CategoryView, ProductView
urlpatterns = [
    path('create_category/', CategoryView.as_view(), name='create_category_api'),
    path('create_product/', ProductView.as_view(), name='create_product_api'),
]