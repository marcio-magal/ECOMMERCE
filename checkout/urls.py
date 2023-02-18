from django.urls import path
from . import views

#checkout/
urlpatterns = [
    path('', views.index),
]
