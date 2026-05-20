from django.shortcuts import render
import requests
from django.http import JsonResponse

def buscar_cnpj(request, cnpj):

    response = requests.get(
        f'https://open.cnpja.com/office/{cnpj}'
    )
    
    return JsonResponse(response.json())

def cadastrar_cliente(request):
    
    return render(request,'cadastro_cliente.html')
