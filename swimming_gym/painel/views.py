from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import  Sum
from pagamentos.models import Pagamento
from painel.tables import ProximosPagamentos, ProximosRecebimentos
from recebimentos.models import Recebimento


@login_required(login_url='login:login', redirect_field_name='next')
def home_view(request):
    proximos_pagamentos = Pagamento.objects.filter(status='pendente').order_by('data_vencimento')[:3]
    proximos_recebimentos = Recebimento.objects.filter(status='pendente').order_by('data_vencimento')[:3]
    total_recebido = Recebimento.objects.filter(status='pago').aggregate(total_recebido=Sum('valor'))['total_recebido']
    total_pago = Pagamento.objects.filter(status='pago').aggregate(total_pago=Sum('valor'))['total_pago']
    saldo = total_recebido - total_pago

    tb_pagamentos = ProximosPagamentos(proximos_pagamentos)
    tb_recebimentos = ProximosRecebimentos(proximos_recebimentos)
    return render(request, 'home.html', context={
        'title': 'Painel',
        'tb_pagamentos': tb_pagamentos,
        'tb_recebimentos': tb_recebimentos,
        'total_faturamento': total_recebido,
        'total_despesas': total_pago,
        'saldo': saldo,
    })
