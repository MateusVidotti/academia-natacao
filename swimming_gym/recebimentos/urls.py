from django.urls import path
from recebimentos import views

app_name = 'recebimentos'

urlpatterns = [
    path('', views.recebimentos_views, name='recebimentos'),
    path('adicionar/', views.adicionar_recebimento, name='adicionar_recebimento'),
    path('editar/<recebimento_id>/', views.editar_recebimento, name='editar_recebimento'),
    path('deletar/<recebimento_id>', views.delete_recebimento, name='deletar_recebimento')
]
