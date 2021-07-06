from .forms import PostForm
from .models import Formulario
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

def Modifi(request,id):
    form = Formulario.objects.get(numeroiD=id)

    datos ={
        'form': PostForm(instance=form)
    }
    if request.method == 'POST': 
        formulario = PostForm(data=request.POST, instance = form)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('ver')
    return render(request, 'core/modificar.html', datos)

def Borrar(request,id):
    form = Formulario.objects.get(numeroId=id)
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