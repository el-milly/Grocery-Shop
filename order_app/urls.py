from django.urls import path
from .views import OrderCreateView, ProductCreateView, CategoryCreateView

urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='order-api'),
    path('create_product/', ProductCreateView.as_view(), name='product-api'),
    path('create_category/', CategoryCreateView.as_view(), name='category-api'),
]