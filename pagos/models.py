from django.db import models
from clientes.models import Cliente
from gestores.models import Gestor

class Pago(models.Model):
    cliente = models.ForeignKey(Cliente,related_name='pagos',on_delete=models.CASCADE)
    gestor = models.ForeignKey(Gestor,related_name='pagos',on_delete=models.CASCADE)
    f_pago = models.DateTimeField()
    monto = models.PositiveIntegerField()
    abonos = models.PositiveIntegerField()

