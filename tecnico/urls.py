
from django.urls import path
from . import views
from .views import salvar

urlpatterns = [
    path('', views.home, name = "home_aluno"),
    path('salvar', salvar, name = "salvar")
]