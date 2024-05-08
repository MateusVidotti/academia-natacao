from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome completo')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    email = models.EmailField(verbose_name='Email')
    celular = models.CharField(max_length=12, verbose_name='Celular')
    endereço = models.TextField()

