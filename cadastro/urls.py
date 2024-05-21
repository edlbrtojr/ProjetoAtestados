from django.urls import path
from cadastro.views import inserir, visualizar, inicio

urlpatterns = [
    path('inserir/', inserir, name='inserir'),
    path('visualizar/', visualizar, name='visualizar'),
    path('', inicio, name='inicio')
]