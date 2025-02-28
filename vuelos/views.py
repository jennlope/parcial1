from django import forms
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Vuelo
from django.db.models import Avg

# Create your views here.

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['nombre', 'tipo', 'precio']
        widgets = {
            'tipo': forms.Select(choices=Vuelo.Tipos)
        }

def index(request):
    return render(request, 'index.html')

def registro_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Vuelo registrado")
            return redirect('lista_vuelos')
    else:
        form = VueloForm()
    return render(request, 'resgistro.html', {'form': form})

def lista_vuelos(request):
    vuelo = Vuelo.objects.all().order_by('precio')
    return render(request, 'lista.html', {'vuelos': vuelo})

def vuelo_estadisticas(request):
    nacional_cuenta = Vuelo.objects.filter(tipo=Vuelo.Nacional).count()
    internacional_cuenta = Vuelo.objects.filter(tipo=Vuelo.Internacional).count()
    nacional_precio = Vuelo.objects.filter(tipo=Vuelo.Nacional).aggregate(Avg('precio'))['precio__avg']
    return render(request, 'estadisticas.html', {
        'nacional_cuenta': nacional_cuenta,
        'internacional_cuenta': internacional_cuenta,
        'nacional_precio': nacional_precio or 0
    })