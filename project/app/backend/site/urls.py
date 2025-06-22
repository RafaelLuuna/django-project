from django.urls import path, include
from . import views as site_views

urlpatterns = [
    path('home/', site_views.home, name='home'),
    path('formulario/', site_views.formulario_exemplo, name='formulario_exemplo'),
    path('tabela/', site_views.tabela_exemplo, name='tabela_exemplo'),
]