from django.urls import path
from .views import equipamentos

urlpatterns = [
    
    path('', equipamentos, name = "equipamentos")
]