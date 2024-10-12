from django.urls import path
from painel import views

app_name = 'painel'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('relatorio_saldo', views.relatorio_saldo, name="relatorio_saldo"),
]