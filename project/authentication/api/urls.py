from django.urls import path, include
from . import views as auth_api_views

urlpatterns = [
    path('login/', auth_api_views.login),
    path('logout/', auth_api_views.logout),
    path('singup/', auth_api_views.singup),
]