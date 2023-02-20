from django.urls import path
from . import views

#cadastrocliente/
urlpatterns = [
    path('', views.index),
]
