from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    TIPO_PESSOA_CHOICES = (
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )

    tipo = models.CharField(max_length=2, choices=TIPO_PESSOA_CHOICES, default='PF')
    documento = models.CharField('CPF/CNPJ', max_length=20, unique=True)
    nome = models.CharField('Nome / Razão Social', max_length=200)
    email = models.EmailField('E-mail', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20)
    
    cep = models.CharField('CEP', max_length=9)
    endereco = models.CharField('Endereço',max_length=255, blank=True)
    numero = models.CharField('Número', max_length=20, blank=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)
    
    data_inicio = models.DateField('Data de Início', default=timezone.now)
    contrato_assinado = models.BooleanField('Contrato Assinado?', default=False)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.documento})"