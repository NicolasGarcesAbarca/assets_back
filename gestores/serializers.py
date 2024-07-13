from .models import Gestor
from rest_framework import serializers

class GestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = ('id','name')