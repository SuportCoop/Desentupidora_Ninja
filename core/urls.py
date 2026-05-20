from django.contrib import admin
from django.urls import path
from laudo.views import visualizar_laudo_print
from crm.views import buscar_cnpj

urlpatterns = [
    path('admin/', admin.site.urls),
    path('laudo/<int:laudo_id>/imprimir/', visualizar_laudo_print, name='visualizar_laudo_print'),
    path('buscar-cnpj/<str:cnpj>/', buscar_cnpj, name='buscar_cnpj')
]
