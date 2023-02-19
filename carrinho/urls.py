from django.urls import path
from . import views

#carrinho/
urlpatterns = [
    path('', views.index),
]
