from django.contrib import admin
from empresas.models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Empresa, EmpresaAdmin)