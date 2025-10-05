from django.urls import path
from django.contrib import admin
from .views import ProductsListView, ProductsShowView, ProductUrlView, CartSendView
urlpatterns = [
    path('main/', ProductsListView.as_view(), name='main_api'),
    path('products/', ProductsShowView.as_view(), name='products_api'),
    path('object/<slug:slug>/', ProductUrlView.as_view(), name='url_api'),
    path('to-cart/', CartSendView.as_view(), name='cart_api'),
]
