from django.contrib import admin
from .models import Pessoa, Contato

@admin.action(description='Ativar todas as Pessoas')
def ativar_todos(modeladmin, request , queryset):
    queryset.update(ativo=True)

@admin.action(description='Desativar todas as Pessoas')
def desativar_todos(modeladmin, request , queryset):
    queryset.update(ativo=False)

# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [
        'ativa',
        'data_nascimento'
    ]
    search_fields = [
        'nome_completo'
    ]
    action = [
        'ativar todos'
        'desativar todos'
    ]


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)