from django.urls import path

from . import views

urlpatterns = [
    path('', views.estabelecimentos ),
    path('loja_1/', views.loja_1 ),
]