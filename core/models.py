from django.db import models

# Create your models here.
opciones_moneda = [
    [0, "Pesos"],
    [1, "Dolares"]
]

class Formulario(models.Model):
    #numeroId = models.IntegerField()
    #thumbnail = models.ImageField()
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    clave = models.CharField(max_length=15)
    moneda = models.IntegerField(choices=opciones_moneda)
    
    def __str__(self):
        return self.nombre
