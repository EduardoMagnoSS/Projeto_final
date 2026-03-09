from django.shortcuts import render, redirect, get_object_or_404
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

def editar_equip(request, id):
    equipamento = Equipamento.objects.get(id=id)
    return render(request, "editar_equip.html",{"equipamento":equipamento})
    
def update_equip(request, id):
    
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == "POST":
        id_remoto = request.POST.get("id_remoto")
        equipamento = Equipamento.objects.get(id=id)
        
        equipamento.tombo = request.POST.get("tombo")
        equipamento.tipo = request.POST.get("tipo")
        equipamento.descricao = request.POST.get("descricao")
        equipamento.setor = request.POST.get("setor")
        equipamento.usuario = request.POST.get("usuario")
    
        equipamento.id_remoto = int(id_remoto) if id_remoto else None
        equipamento.save()
        
        return redirect(equipamentos)
    
    return render(request,"equipamentos.html",{"equipamento":equipamento})
    
def deletar_equip(request, id):
    equipamento = Equipamento.objects.get(id=id)
    equipamento.delete()
    
    return redirect(equipamentos)