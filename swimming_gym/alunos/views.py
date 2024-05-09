from django.shortcuts import render, redirect, get_object_or_404
from alunos.models import Aluno
from alunos.forms import AlunoForm, EditAlunoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login:login', redirect_field_name='next')
def alunos_view(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', context={
        'title': 'Alunos',
        'alunos': alunos
    })


@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request, request.POST)
        if form.is_valid():
            novo_aluno = form.save(commit=False)
            form.save()
            messages.success(request, f'O aluno "{novo_aluno.nome}" foi adicionado com sucesso!')
            return redirect('alunos:alunos')
    else:
        form = AlunoForm(request)

    return render(request, 'adicionar_aluno.html', context={
        'title': 'Adicionar aluno',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    if request.method == 'POST':
        form = EditAlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno_edit = form.save()
            messages.success(request, f'O aluno "{aluno_edit.nome}" foi editado com sucesso!')
            return redirect('alunos:alunos')
    else:
        form = EditAlunoForm(instance=aluno)

    return render(request, 'adicionar_aluno.html', context={
        'title': 'Editar aluno',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def delete_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)
    aluno.delete()
    messages.success(request, f'O aluno foi deletado com sucesso!')
    return redirect('alunos:alunos')
