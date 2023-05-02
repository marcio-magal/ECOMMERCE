from django.urls import path

from . import views


urlpatterns = [
    path('loja-1/', views.loja_1),
    path('loja-2/', views.loja_2),
    path('loja-3/', views.loja_3),
]
