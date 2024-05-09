from django.shortcuts import render, redirect, get_object_or_404
from pagamentos.models import Pagamento
from pagamentos.forms import PagamentoForm, EditPagamentoForm
from django.contrib import messages
from pagamentos.tables import PagamentoTable
from django.contrib.auth.decorators import login_required


@login_required(login_url='login:login', redirect_field_name='next')
def pagamentos_views(request):
    pagamentos = Pagamento.objects.all()
    table = PagamentoTable(pagamentos)
    return render(request, 'pagamentos.html', context={
        'title': 'Pagamentos',
        'table': table
    })


@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request, request.POST)
        if form.is_valid():
            novo_pagamento = form.save(commit=False)
            form.save()
            messages.success(request, f'O pagamento do fornecedor {novo_pagamento.fornecedor.nome}'
                                      f'foi adicionado com sucesso!')
            return redirect('pagamentos:pagamentos')
    else:
        form = PagamentoForm(request)

    return render(request, 'adicionar_pagamento.html', context={
        'title': 'Adicionar pagamento',
        'form': form,
    })


@login_required(login_url='login:login', redirect_field_name='next')
def editar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, pk=pagamento_id)
    if request.method == 'POST':
        form = EditPagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento_edit = form.save()
            messages.success(request, f'O pagamento do fornecedor {pagamento_edit.fornecedor.nome}'
                                      f' foi editado com sucesso!')
            return redirect('pagamentos:pagamentos')
    else:
        form = EditPagamentoForm(instance=pagamento)

    return render(request, 'adicionar_pagamento.html', context={
        'title': 'Editar pagamento',
        'form': form,
        'pagamento': pagamento
    })


@login_required(login_url='login:login', redirect_field_name='next')
def delete_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, pk=pagamento_id)

    pagamento.delete()
    messages.success(request, 'O pagamento foi deletado com sucesso!')
    return redirect('pagamentos:pagamentos')
