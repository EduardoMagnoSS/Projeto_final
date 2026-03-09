from django.urls import path
from .views import equipamentos, salvar_equip, deletar_equip

urlpatterns = [
    
    path('', equipamentos, name = "equipamentos"),
    path('salvar', salvar_equip, name="salvar_equip"),
    path('deletar/<int:id>', deletar_equip, name="deletar_equip")
]