from django.urls import path, include
from .views import teste_crud, salvar, editar, update, delete
from . import views

urlpatterns = [
    path('', views.index),

    path('teste-crud', teste_crud),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
