from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('loja_1/', views.loja_1),
    path('loja_2/', views.loja_2),
]
