
from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from laudo.models import Laudo
from crm.models import Cliente

@staff_member_required # Garante que apenas usuários logados no admin acessem
def visualizar_laudo_print(request, laudo_id):
    laudo = get_object_or_404(Laudo, id=laudo_id)
    cliente = Cliente # Ajuste conforme a relação no seu model
    
    context = {
        'laudo': laudo,
        'cliente': laudo.cliente,
    }
    # Retorna aquele HTML lindo com as cores da Desentupidora Ninja
    return render(request, 'laudo_vazamento.html', context)