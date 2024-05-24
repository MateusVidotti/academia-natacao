from django import forms
from recebimentos.models import Recebimento


class RecebimentoForm(forms.ModelForm):

    class Meta:
        model = Recebimento
        fields = [
            'aluno',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, request, *args, **kwargs):
        super(RecebimentoForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['aluno']


class EditRecebimentoForm(forms.ModelForm):

    class Meta:
        model = Recebimento
        fields = [
            'aluno',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }