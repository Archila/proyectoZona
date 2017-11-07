from django import forms
from .models import Producto, Proveedor

class ProductoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Producto
        fields = ('nombre', 'unidad', 'precio','proveedor')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
    def __init__ (self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["proveedor"].widget = forms.widgets.Select()
#Podemos usar un texto de ayuda en el widget
        self.fields["proveedor"].help_text = "Ingrese los el proveedor del formulario"
#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["proveedor"].queryset = Producto.objects.all()
