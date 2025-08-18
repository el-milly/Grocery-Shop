from .views import CartView
from django.urls import path
urlpatterns = [
    path('create_cart/', CartView.as_view(),name='cart-api'),
]
