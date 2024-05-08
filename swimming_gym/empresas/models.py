from django.db import models


class Empresa(models.Model):
    razao_social = models.CharField(max_length=170, verbose_name='Razão social')
    nome_fantasia = models.CharField(max_length=170, verbose_name='Nome fantasia')
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    ie = models.CharField(max_length=9, verbose_name='Inscrição estadual')
    telefone_fixo = models.CharField(max_length=10, verbose_name='Telefone fixo', blank=True)
    telefone_movel = models.CharField(max_length=12, verbose_name='Telefone móvel')
    observacao = models.CharField(max_length=255, verbose_name='Observação', blank=True)

    def __str__(self):
        return self.nome_fantasia
