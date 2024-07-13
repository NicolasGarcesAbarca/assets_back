from .models import Pago
from rest_framework import serializers

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['cliente','gestor','f_pago','monto','abonos']