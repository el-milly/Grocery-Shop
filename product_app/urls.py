from django.urls import path
from .views import CategoryView
urlpatterns = [
    path('create_category/', CategoryView.as_view(), name='create_category_api'),
]