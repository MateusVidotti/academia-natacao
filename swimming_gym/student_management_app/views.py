from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd


def show_demo_page(request):
    return render(request, 'demo.html')


def show_login_page(request):
    return render(request, 'login_page.html')


def do_login(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método Não Permitido</h2>')
    else:
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password')
                                         )
        if user is not None:
            login(request, user)
            if user.user_type == '1':
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == '2':
                return HttpResponse('Staff login')
            else:
                return HttpResponse('Student login')
        else:
            messages.error(request, 'Dados de Login Inválidos')
            return HttpResponseRedirect('/')


def get_user_details(request):
    if request.user is not None:
        return HttpResponse('User : ' + request.user.email + 'usertype :' + request.user.user_type)
    else:
        return HttpResponse('Por favor faça o login.')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



