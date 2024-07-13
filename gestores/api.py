from .models import Gestor
from rest_framework import viewsets,permissions
from .serializers import GestorSerializer

class GestorViewSet(viewsets.ModelViewSet):
    queryset = Gestor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GestorSerializer