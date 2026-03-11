from django.shortcuts import render, redirect

from equipamentos.models import Equipamento
from tecnico.models import tecnico
from .models import Atendimento

# Create your views here.
def atendimentos (request):
    atendimentos = Atendimento.objects.all()
    equipamentos = Equipamento.objects.all()
    tecnicos = tecnico.objects.all()
    
    return render(request, "atendimento.html",{"atendimentos":atendimentos,"equipamentos":equipamentos,"tecnicos":tecnicos})


def salvar_atend(request):
    
    equipamento_id = request.POST.get("equipamento")
    responsavel_id = request.POST.get("responsavel")
    problema = request.POST.get("problema")
    solucao = request.POST.get("solucao")
    observacao = request.POST.get("observacao") or None
    
    Atendimento.objects.create(equipamento_id=equipamento_id,problema=problema,solucao=solucao,observacao=observacao,responsavel_id=responsavel_id)
    
    atendimentos = Atendimento.objects.all()
    equipamentos = Equipamento.objects.all()
    tecnicos = tecnico.objects.all()
    
    return render(request,"atendimento.html",{"atendimentos": atendimentos,"equipamentos":equipamentos,"tecnicos":tecnicos})

def delete_atend(request,id):
    atendimento = Atendimento.objects.get(id=id)
    
    atendimento.delete()
    
    return redirect(atendimentos)

def edit_atend(request,id):
    atendimento = Atendimento.objects.get(id=id)
    equipamentos = Equipamento.objects.all()
    tecnicos = tecnico.objects.all()
    
    return render(request,"editar_atend.html",{"atendimento":atendimento, "equipamentos":equipamentos, "tecnicos":tecnicos})

def update_atend(request,id):
    atendimento = Atendimento.objects.get(id=id)
    
    atendimento.equipamento_id = request.POST.get("equipamento")
    atendimento.responsavel_id = request.POST.get("responsavel")
    atendimento.problema = request.POST.get("problema")
    atendimento.solucao = request.POST.get("solucao")
    atendimento.observacao = request.POST.get("observacao") or None
    atendimento.save()
    
    return redirect(atendimentos)    