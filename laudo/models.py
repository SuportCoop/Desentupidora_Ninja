from django.db import models
from crm.models import Cliente

# Create your models here.
class Procedimentos (models.Model):
    nome = models.CharField(verbose_name='Tipo de procedimentos',max_length=50)
    
    def __str__(self):
        return self.nome

class Laudo (models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT,verbose_name='Cliente')
    data_inspecao = models.DateField(verbose_name='Data Inspeção')
    procedimentos = models.ManyToManyField(Procedimentos, verbose_name='Procedimento de Localização')
    vazamento_detectado = models.BooleanField(verbose_name='Vazamento Detectado')
    area_vazamento=models.CharField(verbose_name='Localização do Vazamento')
    vazamento= models.CharField(verbose_name='Local do vazamento')
    observacao= models.TextField(verbose_name='Observações')