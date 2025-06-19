from django.urls import path, include
from . import views as auth_api_views

urlpatterns = [
    path('login/', auth_api_views.LoginApi),
    path('logout/', auth_api_views.LogoutApi),
    path('singup/', auth_api_views.SingupApi),
]