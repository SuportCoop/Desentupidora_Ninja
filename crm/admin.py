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
            
            'fields': (
                ('cep', 'uf'), 
                'endereco', 
                ('numero', 'bairro'), 
                'cidade',
            )
        }),
        ('Status', {
            'fields': ('data_inicio', 'contrato_assinado', 'ativo')
        }),
    )
    
    class Media:
        js = ('js/buscar_cep.js',)
        js2 = ('js/buscar_cnpj.js')