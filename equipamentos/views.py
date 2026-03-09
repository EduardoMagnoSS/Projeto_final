from django.shortcuts import render, redirect
from .models import Equipamento

# Create your views here.
def equipamentos(request):
    equipamentos = Equipamento.objects.all()
    
    return render(request, "equipamentos.html",{"equipamentos":equipamentos})

def salvar_equip(request):
    tombo = request.POST.get("tombo")
    tipo = request.POST.get("tipo")
    descricao = request.POST.get("descricao")
    setor = request.POST.get("setor")
    usuario = request.POST.get("usuario")
    id_remoto = request.POST.get("id_remoto")
    
    id_remoto = int(id_remoto) if id_remoto else None
    Equipamento.objects.create(tombo=tombo, tipo=tipo, descricao=descricao, setor=setor, usuario=usuario, id_remoto=id_remoto)
    equipamentos = Equipamento.objects.all()
    
    return render(request, "equipamentos.html", {"equipamentos":equipamentos})

def deletar_equip(request, id):
    equipamento = Equipamento.objects.get(id=id)
    equipamento.delete()
    return redirect(equipamentos)