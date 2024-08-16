from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('list_categorias/', views.list_categorias),

    path('list_categorias/<int:id>', views.detail_categoria),
    path('list_productos/', views.list_productos),
    path('list_productos/add', views.add_productos),
    path('list_productos/<int:id>', views.detail_productos),
    path('list_productos/<int:id>/delete', views.delete_productos),
    path('list_productos/<int:id>/update', views.update_productos),
    path('dashboard', views.dashboard),
    path('productos_por_vencer', views.prodcuts_por_vencer)
]
