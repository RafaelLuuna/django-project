from django.urls import path, include
from . import views as site_views

urlpatterns = [
    path('home/', site_views.home),
]