from django.contrib import admin
from .models import Tipo, Proveedor, Producto, Actividad, Cotizacion

# Register your models here.
admin.site.register(Tipo)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Actividad)
admin.site.register(Cotizacion)
