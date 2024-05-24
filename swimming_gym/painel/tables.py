import django_tables2 as tables
from pagamentos.models import Pagamento
from recebimentos.models import Recebimento


class ProximosPagamentos(tables.Table):
    fornecedor = tables.Column(verbose_name='Fornecedor', orderable=False)
    descricao = tables.Column(verbose_name='Descrição', orderable=False)
    valor = tables.Column(verbose_name='Valor', orderable=False)
    data_vencimento = tables.Column(verbose_name='Data de vencimento', orderable=False)
    status = tables.Column(verbose_name='Status', orderable=False)

    class Meta:
        model = Pagamento
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('fornecedor', 'descricao', 'valor', 'status')


class ProximosRecebimentos(tables.Table):
    aluno = tables.Column(verbose_name='Aluno', orderable=False)
    descricao = tables.Column(verbose_name='Descrição', orderable=False)
    valor = tables.Column(verbose_name='Valor', orderable=False)
    data_vencimento = tables.Column(verbose_name='Data de vencimento', orderable=False)
    status = tables.Column(verbose_name='Status', orderable=False)

    class Meta:
        model = Recebimento
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('aluno', 'descricao', 'valor', 'status')