from django.urls import path
from rest_framework import routers
from .api import PropertyViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'properties', PropertyViewSet)

urlpatterns = []

urlpatterns = router.urls + urlpatterns

