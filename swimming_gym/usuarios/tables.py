import django_tables2 as tables
from usuarios.models import CustomUser


class UsuarioTable(tables.Table):
    nome = tables.Column(verbose_name='Nome', orderable=False)
    email = tables.Column(verbose_name='E-mail', orderable=False)
    is_admin = tables.Column(verbose_name='Admin', orderable=False)
    is_comum = tables.Column(verbose_name='Comum', orderable=False)
    opcao = tables.TemplateColumn(template_name='botao_acoes_usuarios.html', verbose_name='Opções', orderable=False)

    class Meta:
        model = CustomUser
        attrs = {'class': 'table table-bordered table-hover'}
        fields = ('nome', 'email', 'is_admin', 'is_comum')