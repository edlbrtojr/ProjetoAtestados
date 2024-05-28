from django.shortcuts import render
from cadastro.forms import InserirForm
from django.shortcuts import redirect

def inserir(request):
    if request.method == 'POST':
        form = InserirForm(request.POST)
        if form.is_valid():
            form.save()
    
    
    return render(request, 'cadastro/inserir.html', {"form": InserirForm})

def visualizar(request):
    return render(request, 'cadastro/visualizar.html')

def inicio(request):
    return render(request, 'cadastro/inicio.html')
