from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login:login', redirect_field_name='next')
def home_view(request):
    return render(request, 'home.html', context={
        'title': 'Painel',
    })
