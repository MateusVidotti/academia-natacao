from django import forms
from pagamentos.models import Pagamento


class PagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        fields = [
            'fornecedor',
            'descricao',
            'valor',
            'data_vencimento',
            'status',
        ]
        widgets = {
            'data_vencimento': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, request, *args, **kwargs):
        super(PagamentoForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['fornecedor']


class EditPagamentoForm(forms.ModelForm):

    class Meta:
        model = Pagamento
        fields = [
            'fornecedor',
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
