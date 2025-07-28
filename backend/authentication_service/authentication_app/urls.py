from django.urls import path
from .views import UserViewApi, UserLoginView, CheckView
from knox import views as knox_views


urlpatterns = [
    path('create/', UserViewApi.as_view(), name='user-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout-api'),
    path('check/', CheckView.as_view(), name='check-api')
]