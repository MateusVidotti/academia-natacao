from django import forms
from alunos.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'telefone',
            'documento',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]

    def __init__(self, request, *args, **kwargs):
        super(AlunoForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['nome']


class EditAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'telefone',
            'documento',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]