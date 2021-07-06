from django.urls import path, include
from . import views
from .views import Ingresar, Ver, Modifi, Borrar, PostCreateView

urlpatterns=[
    path('', views.Index, name='index'),
    path('ingresar', Ingresar, name="ingresar"),
    path('ver', Ver, name="ver"),
    path('modificar/<id>', Modifi, name="modificar"),
    path('eliminar/<id>', Borrar, name="eliminar"), 
    path('create', PostCreateView.as_view(), name='create'),
]