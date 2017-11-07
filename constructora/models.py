from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Proveedor (models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Tipo (models.Model):
    nombre =   models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre    = models.CharField(max_length=30)
    unidad    = models.CharField(max_length=20)
    marca    = models.CharField(max_length=30)
    precio      = models.CharField(max_length=10)
    proveedor   = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    tipo =  models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):

    nombre    = models.CharField(max_length=30)
    productos = models.ManyToManyField(Producto, through='Cotizacion')

    def __str__(self):
        return self.nombre

class Cotizacion (models.Model):

    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.IntegerField()
    total = models.CharField(max_length=10)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
