"""
URL configuration for swimming_gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('painel.urls')),
    # path('produtos/', include('app_produtos.urls')),
    # path('clientes/', include('app_clientes.urls')),
    # path('fornecedores/', include('app_fornecedores.urls')),
    # path('pagamentos/', include('app_pagamentos.urls')),
    # path('recebimentos/', include('app_recebimentos.urls')),
    # path('empresas/', include('app_empresas.urls')),
    #path('usuarios/', include('usuarios.urls')),
    path('login/', include('login.urls')),
    # path('pedidos/', include('app_pedidos.urls')),
]
