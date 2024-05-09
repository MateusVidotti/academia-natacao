import django_tables2 as tables
from pagamentos.models import Pagamento


class PagamentoTable(tables.Table):
    fornecedor = tables.Column(verbose_name='Fornecedor', orderable=False)
    data_emissao = tables.Column(verbose_name='Data emissão', orderable=False)
    data_vencimento = tables.Column(verbose_name='Data de vencimento', orderable=False)
    status = tables.Column(verbose_name='Status', orderable=False)
    opcao = tables.TemplateColumn(template_name='botao_acoes.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = Pagamento
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('fornecedor', 'data_emissao', 'data_vencimento', 'status', 'valor')