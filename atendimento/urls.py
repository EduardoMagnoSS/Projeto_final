from django.urls import path
from . import views

urlpatterns = [
    path('',views.atendimentos, name="atendimento"),
    path('salvar_atend',views.salvar_atend,name="salvar_atend")
]