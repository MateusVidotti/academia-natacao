from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuarios_view, name='usuarios'),
    path('adicionar/', views.adicionar_usuario, name='adicionar_usuario'),
    path('editar/<usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('editar/password/<usuario_id>/', views.editar_senha_usuario, name='editar_password'),
    path('deletar/<usuario_id>', views.deletar_usuario, name='deletar_usuario')
]
