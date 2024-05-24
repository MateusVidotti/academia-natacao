from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from recebimentos.models import Recebimento
from recebimentos.forms import RecebimentoForm, EditRecebimentoForm
from recebimentos.tables import RecebimentoTable


@login_required(login_url='login:login', redirect_field_name='next')
def recebimentos_views(request):
    recebimentos = Recebimento.objects.all()
    table = RecebimentoTable(recebimentos)
    return render(request, 'recebimentos.html', context={
        'title': 'Recebimentos',
        'table': table
    })


@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_recebimento(request):
    if request.method == 'POST':
        form = RecebimentoForm(request, request.POST)
        if form.is_valid():
            novo_recebimento = form.save(commit=False)
            form.save()
            messages.success(request,
                             f'O recebimento do aluno "{novo_recebimento.aluno.nome}" foi adicionado com sucesso! ')
            return redirect('recebimentos:recebimentos')
    else:
        form = RecebimentoForm(request)

    return render(request, 'adicionar_recebimento.html', context={
        'title': 'Adicionar recebimentos',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def editar_recebimento(request, recebimento_id):
    recebimento = get_object_or_404(Recebimento, pk=recebimento_id)
    if request.method == 'POST':
        form = EditRecebimentoForm(request.POST, instance=recebimento)
        if form.is_valid():
            edit_recebimento = form.save()
            messages.success(request,
                             f'O recebimento do aluno "{edit_recebimento.aluno.nome}" foi editado com sucesso!')
            return redirect('recebimentos:recebimentos')
    else:
        form = EditRecebimentoForm(instance=recebimento)

    return render(request, 'adicionar_recebimento.html', context={
        'title': 'Editar recebimento',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def delete_recebimento(request, recebimento_id):
    recebimento = get_object_or_404(Recebimento, pk=recebimento_id)

    recebimento.delete()
    messages.success(request, f'O recebimento foi deletado com sucesso!')
    return redirect('recebimentos:recebimentos')


@login_required(login_url='login:login', redirect_field_name='next')
def relatorio_faturamento(request):
    x = Recebimento.objects.filter(status='pago')
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        y = sum([i.valor for i in x if i.data_vencimento.month == mes and i.data_vencimento.year == ano])
        labels.append(meses[mes - 1])
        data.append(y)
        cont += 1
    data_json = {'data': data[::-1], 'labels': labels[::-1]}
    return JsonResponse(data_json)
