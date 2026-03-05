from django.shortcuts import render, redirect
from .models import tecnico

# Create your views here.
def home(request):
    tecnicos = tecnico.objects.all()
    
    return render(request, "tecnico/home.html",{"tecnicos": tecnicos})

def salvar(request):
    nome = request.POST.get("nome")
    matricula = request.POST.get("matricula")
    tecnico.objects.create(nome = nome, matricula = matricula)
    tecnicos = tecnico.objects.all()
    
    return render (request,"tecnico/home.html",{"tecnicos": tecnicos})

def editar(request, id):
    tecnico_ = tecnico.objects.get(id=id)
    
    return render(request, "tecnico/editar.html", {"tecnico": tecnico_})

def update (request, id):
    nome = request.POST.get("nome")
    matricula = request.POST.get("matricula")
    tecnico_ = tecnico.objects.get(id=id)
    tecnico_.nome = nome
    tecnico_.matricula = matricula
    tecnico_.save()
    return redirect(home)

def deletar (request, id):
    tecnico_ = tecnico.objects.get(id=id)
    tecnico_.delete()
    return redirect(home)