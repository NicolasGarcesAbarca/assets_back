from rest_framework import routers
from .api import PagoViewSet

router = routers.DefaultRouter()
router.register('api/pagos',PagoViewSet,'pagos')

urlpatterns = router.urls