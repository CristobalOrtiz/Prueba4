from django import forms
from .models import Formulario

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Formulario
        #fields = ["numeroId","foto","nombre","telefono","direccion","email","pais","clave","moneda"]
        fields = ('__all__')