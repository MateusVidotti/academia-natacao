from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import CustomUser
from usuarios.forms import CustomUserCreationForm, EditCustomUserCreationForm
from usuarios.tables import UsuarioTable
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login:login', redirect_field_name='next')
def usuarios_view(request):
    usuarios = CustomUser.objects.all()
    table = UsuarioTable(usuarios)
    return render(request, 'usuarios.html', context={
        'title': 'Usuários',
        'table': table
    })


@login_required(login_url='login:login', redirect_field_name='next')
def adicionar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request, request.POST)
        if form.is_valid():
            novo_usuario = form.save(commit=False)
            form.save()
            messages.success(request, f'O novo usuário "{novo_usuario.nome}" foi adicionado com sucesso! ')
            return redirect('usuarios:usuarios')
    else:
        form = CustomUserCreationForm(request)
    return render(request, 'adicionar_usuario.html', context={
        'title': 'Adicionar usuário',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, pk=usuario_id)
    if request.method == 'POST':
        form = EditCustomUserCreationForm(request.POST, instance=usuario)
        if form.is_valid():
            edit_usuario = form.save()
            messages.success(request, f'O usuário "{edit_usuario.nome}" foi editado com sucesso!')
            return redirect('usuarios:usuarios')
    else:
        form = EditCustomUserCreationForm(instance=usuario)
    return render(request, 'adicionar_usuario.html', context={
        'title': 'Editar usuario',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def editar_senha_usuario(request, usuario_id):
    usuario = CustomUser.objects.get(pk=usuario_id)
    if request.method == 'POST':
        form = SetPasswordForm(user=usuario, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'A senha do usuário foi alterada com sucesso!')
            return redirect('usuarios:usuarios')
    else:
        form = SetPasswordForm(user=usuario)
    return render(request, 'adicionar_usuario.html', context={
        'title': f'Editar senha do usuário {CustomUser.nome}',
        'form': form
    })


@login_required(login_url='login:login', redirect_field_name='next')
def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(CustomUser, pk=usuario_id)

    usuario.delete()
    messages.success(request, f'O usuário foi deletado com sucesso!')
    return redirect('usuarios:usuarios')