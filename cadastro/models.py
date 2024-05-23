from django.conf import settings
from django.db import models

class InserirFalta(models.Model):
    nome_aluno = models.CharField(max_length= 100, null=False, blank=False)
    ano_aluno = models.IntegerField()
    turma_aluno = models.CharField(max_length=3, null=False, blank=False)
    data_afastamente = models.DateField()
    dias_afastado = models.IntegerField( null=False, blank=False)
    justificativa = models.TextField(null=False, blank=False)
    arquivo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Cadastrado [nome_aluno={self.nome_aluno}] "