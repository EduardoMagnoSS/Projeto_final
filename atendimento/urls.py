from django.urls import path
from . import views

urlpatterns = [
    path('',views.atendimentos, name="atendimento"),
    path('salvar_atend',views.salvar_atend,name="salvar_atend"),
    path('delete_atend/<int:id>',views.delete_atend,name="delete_atend"),
    path('edit_tend/<int:id>',views.edit_atend, name="edit_atend"),
    path('update_atend/<int:id>',views.update_atend,name="update_atend")
]