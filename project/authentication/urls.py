from django.urls import path, include
from . import views as auth_views

urlpatterns = [
    path('login/', auth_views.login),
    path('cadastro/', auth_views.cadastro),
]