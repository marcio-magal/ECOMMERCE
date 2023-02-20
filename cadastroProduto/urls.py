from django.urls import path
from . import views

#cadastroproduto/
urlpatterns = [
    path('', views.index),
]
