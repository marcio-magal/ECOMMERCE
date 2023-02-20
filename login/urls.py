from django.urls import path
from . import views

#login/
urlpatterns = [
    path('', views.index),
]
