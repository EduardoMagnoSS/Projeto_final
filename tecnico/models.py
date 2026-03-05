from django.db import models

# Create your models here.
class tecnico(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=13)
    
    def __str__(self):
        return self.nome