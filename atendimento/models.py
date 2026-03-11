from django.db import models
from equipamentos.models import Equipamento
from tecnico.models import tecnico

# Create your models here.
class Atendimento (models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete= models.CASCADE)
    problema = models.TextField()
    solucao = models.TextField()
    observacao = models.TextField(blank=True, null=True, default="")
    data = models.DateField(auto_now_add=True)
    responsavel = models.ForeignKey(tecnico, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.problema