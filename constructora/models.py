from django.db import models
from django.utils import timezone
# Create your models here.

class Proveedor (models.Model):
    nombre  =   models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre    = models.CharField(max_length=60)
    precio      = models.IntegerField()
    actores   = models.ManyToManyField(Actor, through='Actuacion')

    def __str__(self):
        return self.nombre

class Actuacion (models.Model):

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)


class ActuacionInLine(admin.TabularInline):
    model = Actuacion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class ActorAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class PeliculaAdmin (admin.ModelAdmin):
    inlines = (ActuacionInLine,)
