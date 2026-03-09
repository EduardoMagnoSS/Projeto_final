from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.equipamentos, name = "equipamentos"),
    path('salvar', views.salvar_equip, name="salvar_equip"),
    path('deletar/<int:id>', views.deletar_equip, name="deletar_equip"),
    path('editar/<int:id>', views.editar_equip, name="editar_equip"),
    path('update/<int:id>', views.update_equip, name="update_equip")
]