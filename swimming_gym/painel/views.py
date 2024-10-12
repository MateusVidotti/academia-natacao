from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http.response import JsonResponse
from django.shortcuts import render
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


@login_required(login_url='login:login', redirect_field_name='next')
def relatorio_saldo(request):
    recebimentos = Recebimento.objects.filter(status='pago')
    pagamentos = Pagamento.objects.filter(status='pago')
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        recebimento = sum([i.valor for i in recebimentos if i.data_vencimento.month == mes and
                           i.data_vencimento.year == ano])
        pagamento = sum([i.valor for i in pagamentos if i.data_vencimento.month == mes and
                           i.data_vencimento.year == ano])
        saldo = recebimento - pagamento
        labels.append(meses[mes - 1])
        data.append(saldo)
    data_json = {'data': data[::-1],
                 'labels': labels[::-1]}
    return JsonResponse(data_json)
