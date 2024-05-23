from django.shortcuts import render
from cadastro.forms import InserirForm
from django.shortcuts import redirect

def inserir(request):
    if request.POST:
        form = InserirForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect(inicio)
    
    return render(request, 'cadastro/inserir.html', {"form": InserirForm})

def visualizar(request):
    return render(request, 'cadastro/visualizar.html')

def inicio(request):
    return render(request, 'cadastro/inicio.html')
