from django.urls import path
from fornecedores import views

app_name = 'fornecedores'

urlpatterns = [
    path('', views.fornecedores_view, name='fornecedores'),
    path('adicionar', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('editar/<fornecedor_id>', views.editar_fornecedor, name='editar_fornecedor'),
    path('deletar/<fornecedor_id>', views.delete_fornecedor, name='deletar_fornecedor'),
]
