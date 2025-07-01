from django.urls import path
from .views import CategoryView
urlpatterns = [
    path('create_product/', CategoryView.as_view(), name='create_product_api'),
]