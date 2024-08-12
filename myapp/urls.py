from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('lista_categorias', views.list_categorias),
    path('lista_productos', views.list_productos),
    path('lista_productos/<int:id>', views.detail_productos),
]
