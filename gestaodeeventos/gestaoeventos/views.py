from django.shortcuts import render
from .forms import RegistroEvento

# Create your views here.

eventos = []

def registro(request):
    global eventos
    
    if request.method == "POST":
        form = RegistroEvento(request.POST)
        if form.is_valid():
            nomedoevento = form.cleaned_data['nomedoevento']
            local = form.cleaned_data['local']
            eventos.append({"nomedoevento" : nomedoevento, "local" : local})
    else:
        form = RegistroEvento()

    return render(request, 'gestaoeventos/novo.html', {"form" : form})

def dashboard(request):
    return render(request, 'gestaoeventos/home.html', {"eventos" : eventos})