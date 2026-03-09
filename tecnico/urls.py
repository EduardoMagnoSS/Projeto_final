
from django.urls import path
from .views import salvar, editar, update, deletar, tecnico__

urlpatterns = [
    path('', tecnico__, name = 'tecnico'),
    path('salvar', salvar, name = 'salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name ='update'),
    path('delete/<int:id>', deletar, name = 'deletar')
]