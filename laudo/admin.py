from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from laudo.models import Laudo, Procedimentos

# Register your models here.
@admin.register(Laudo)
class LaudoAdmin(admin.ModelAdmin):
    list_display = ('cliente','data_inspecao','vazamento_detectado',)
    actions = ['visualizar_laudo']
     
    @admin.action(description='Visualizar/Imprimir Laudo Técnico')
    def visualizar_laudo(self, request, queryset):
        if queryset.count() > 1:
            messages.error(request, "Selecione apenas UM laudo por vez para visualizar.")
            return

        laudo = queryset.first()
        
        # Redireciona o usuário direto para a página do laudo
        url_laudo = reverse('visualizar_laudo_print', args=[laudo.id])
        return HttpResponseRedirect(url_laudo)
 
@admin.register(Procedimentos)
class ProcedimentosAdmin(admin.ModelAdmin):
    list_display = ('nome',)