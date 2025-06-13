from django.urls import path 
from . import views

urlpatterns = [
    path('', views.listarComunas, name='listarComunas'),
    path('create/', views.comuna_create, name = 'comuna_create'),
    path('update/<int:pk>/', views.comuna_update, name= 'comuna_update'),
    path('delete/<int:pk>/', views.comuna_delete, name='comuna_delete'),
]
