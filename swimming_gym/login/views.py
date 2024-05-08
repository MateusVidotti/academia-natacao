from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard:home')
        messages.error(request, 'Credencias invalidas')
        return redirect('login:login')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login:login')