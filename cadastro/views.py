from django.shortcuts import render
from cadastro.forms import InserirForm

def inserir(request):
    form = InserirForm()
    return render(request, 'cadastro/inserir.html', {"form": form})

def visualizar(request):
    return render(request, 'cadastro/visualizar.html')

def inicio(request):
    return render(request, 'cadastro/inicio.html')
