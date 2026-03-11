from django.shortcuts import render

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
    
    print("equipamento_id:",equipamento_id)
    print("responsavel_id:",responsavel_id)
    
    Atendimento.objects.create(equipamento_id=equipamento_id,problema=problema,solucao=solucao,observacao=observacao,responsavel_id=responsavel_id)
    
    atendimentos = Atendimento.objects.all()
    equipamentos = Equipamento.objects.all()
    tecnicos = tecnico.objects.all()
    
    return render(request,"atendimento.html",{"atendimentos": atendimentos,"equipamentos":equipamentos,"tecnicos":tecnicos})