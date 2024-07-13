from .models import Pago
from rest_framework import viewsets,permissions
from .serializers import PagoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer