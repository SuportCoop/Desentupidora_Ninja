from django.contrib import admin
from crm.models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'documento', 'tipo', 'telefone', 'data_inicio', 'contrato_assinado', 'ativo')
    list_filter = ('tipo', 'ativo', 'contrato_assinado', 'data_inicio')
    search_fields = ('nome', 'documento', 'email')
    list_editable = ('contrato_assinado', 'ativo')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('tipo', 'documento', 'nome', 'email', 'telefone')
        }),
        ('Endereço', {
            # Adicione todos os campos aqui para o JS funcionar
            'fields': (
                ('cep', 'uf'), # Em uma linha
                'endereco', 
                ('numero', 'bairro'), # Em outra linha
                'cidade',
            )
        }),
        ('Status', {
            'fields': ('data_inicio', 'contrato_assinado', 'ativo')
        }),
    )
    
    class Media:
        js = ('js/buscar_cep.js',)