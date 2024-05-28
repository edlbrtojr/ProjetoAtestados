from django.conf import settings
from django.db import models

class InserirFalta(models.Model):
    choices_ano = (('6', '6º ano'), ('7', '7º ano'), ('8', '8º ano'), ('9', '9º ano'))
    choices_turma = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                     ('E', 'E'), ('F', 'F'), ('APC', 'Aprender é o caminho'))
    
    nome_aluno = models.CharField(max_length= 100, null=False, blank=False)
    ano_aluno = models.IntegerField()
    turma_aluno = models.TextChoices("")
    data_afastamente = models.DateField()
    dias_afastado = models.IntegerField( null=False, blank=False)
    justificativa = models.TextField(null=False, blank=False)
    arquivo = models.FileField()

    def __str__(self):
        return f"Cadastrado [nome_aluno={self.nome_aluno}] "