from django.shortcuts import render
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