from rest_framework import viewsets
from scheduler.apps.schedule.models import Property
from .serializers import *
from .filters import *

class PropertyViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Property
    """
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    filterset_class = PropertyFilter