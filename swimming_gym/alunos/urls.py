from django.urls import path
from alunos import views

app_name = 'alunos'

urlpatterns = [
    path('', views.alunos_view, name='alunos'),
    path('adicionar', views.adicionar_aluno, name='adicionar_aluno'),
    path('editar/<aluno_id>', views.editar_aluno, name='editar_aluno'),
    path('deletar/<aluno_id>', views.delete_aluno, name='deletar_aluno'),
]
