from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Producto
from .models import Actividad
from .models import Cotizacion
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'constructora/home.html')
# Create your views here.
