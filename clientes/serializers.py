from .models import Cliente
from rest_framework import serializers
from pagos.serializers import PagoSerializer

class ClienteSerializer(serializers.ModelSerializer):
    pagos = PagoSerializer(many= True,read_only=True)
    class Meta:
        model = Cliente
        fields = ['name','rut','pagos']