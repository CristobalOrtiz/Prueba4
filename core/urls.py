from django.urls import path, include
from . import views
from .views import Ingresar, Ver, Modifi, Borrar, PostCreateView, lista_formularios, xd

urlpatterns=[
    path('', views.Index, name='index'),
    path('ingresar', Ingresar, name="ingresar"),
    path('ver', Ver, name="ver"),
    path('modificar/<nombre>', Modifi, name="modificar"),
    path('eliminar/<nombre>', Borrar, name="eliminar"), 
    path('create', PostCreateView.as_view(), name='create'),
    path('lista_formularios', lista_formularios, name="lista_formularios"),
    path('xd', xd, name="xd")
]