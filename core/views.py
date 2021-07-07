from .forms import PostForm
from .models import Formulario
from django.views.decorators import csrf
from rest_framework.serializers import Serializer
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView



# Create your views here.
def Index(request):
    return render(request, 'index.html')
def Ingresar(request):
    data = {
        'form': PostForm
    }
    if request.method == 'POST': 
        formulario = PostForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Formulario guardado"
            return redirect('index.html')
        else:
           data["form"]= formulario
    return render(request, 'core/crear.html', data)

def Ver(request):
    form = Formulario.objects.all()

    return render(request, 'core/ver.html', context={'form':form})

def Modifi(request,nombre):
    form = Formulario.objects.get(nombre=nombre)

    datos ={
        'form': PostForm(instance=form)
    }
    if request.method == 'POST': 
        formulario = PostForm(data=request.POST, instance = form)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('ver')
    return render(request, 'core/modificar.html', datos)

def Borrar(request,nombre):
    form = Formulario.objects.get(nombre=nombre)
    form.delete()
    return redirect('ver')

class PostCreateView(CreateView):
    form_class = PostForm
    model = Formulario
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Crear'
        })
        return context
    
'''serializers'''
from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import FormularioSerializer
from django.http import JsonResponse

@csrf_exempt
@api_view(['GET', 'POST'])



def lista_formularios(request): 
    if request.method== 'GET':
        formulario = Formulario.objects.all()
        serializer =FormularioSerializer(formulario, many=True)
        return Response(serializer.data)

    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = FormularioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def xd(request):
    usuarios = Formulario.objects.all()
    parsed = FormularioSerializer(usuarios, many=True)
    data = JsonResponse(parsed.data, safe=False)
    return data

def lista_api(request):
    return render(request, 'ApiWeb.html')