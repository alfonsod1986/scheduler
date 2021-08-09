from django.urls import path
from rest_framework import routers
from .api import PropertyViewSet, ActivityViewSet

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = []

urlpatterns = router.urls + urlpatterns

