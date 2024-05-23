from django import forms

class InserirForm(forms.Form):
    choices_ano = (('6', '6º ano'), ('7', '7º ano'), ('8', '8º ano'), ('9', '9º ano'))
    choices_turma = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'),
                     ('E', 'E'), ('F', 'F'), ('APC', 'Aprender é o caminho'))
    nome_aluno=forms.CharField(
        label="Nome do Aluno",
        max_length=100,
        required=True
    )
    ano_aluno=forms.ChoiceField(
        required=True,
        label="Ano",
        choices=choices_ano
    )

    turma_aluno=forms.ChoiceField(
    required=True,
    label="Turma",
    choices=choices_turma
    )

    data_afastamento=forms.DateField(
        required=True,
        label="Data do Afastamento"
    )

    dias_afastados=forms.NumberInput(

        )

    justificativa=forms.CharField(
        widget=forms.Textarea,
        required=True,
        label="Justificativa e Comentários"
    )

    anexos=forms.ImageField(
        widget=forms.FileInput(),
        label="Anexo(s)"
    )

    # Fazer o Responsável pelo registro

    