from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Equipamento(models.Model):
    tombo = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(999999)], unique=True)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)
    usuario = models.CharField(max_length=100, blank=True)
    id_remoto = models.PositiveBigIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.descricao