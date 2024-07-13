from rest_framework import routers
from .api import GestorViewSet

router = routers.DefaultRouter()
router.register('api/gestores',GestorViewSet,'gestores')

urlpatterns = router.urls