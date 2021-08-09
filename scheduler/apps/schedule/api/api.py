from datetime import datetime
from rest_framework import viewsets, status
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from scheduler.apps.schedule.models import Property, Activity
from rest_framework.response import Response
from ..constants import DISABLED, LOCAL_TZ, UTC_TZ
from ..functions import is_activity_lasts_a_maximum_one_hour
from .serializers import *
from .filters import *

class PropertyViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Property
    """
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    filterset_class = PropertyFilter


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet de Activity
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                property_id = request.data.get('property_id')
                schedule = request.data.get('schedule')
                schedule_datetime = UTC_TZ.localize(datetime.strptime(schedule, '%Y-%m-%dT%H:%M:%S.%fZ'))
                schedule_date = schedule[:10]
                prop = Property.objects.get(pk=property_id)

                print(schedule_datetime)

                if prop.status == DISABLED:
                    return Response(data={'message': _("La propiedad que intenta ingresar está desactivada")},
                                        status=status.HTTP_400_BAD_REQUEST)

                activities = Activity.objects.filter(property_id=property_id, schedule__date=schedule_date).order_by('schedule')

                if activities:
                    for activity in activities:
                        if schedule_datetime > activity.schedule:
                            if not is_activity_lasts_a_maximum_one_hour(activity.schedule, schedule_datetime):
                               return Response(data={'message': _("La actividad debe durar 1 hora como máximo")},
                                        status=status.HTTP_400_BAD_REQUEST)
                        if activity.schedule == schedule_datetime:
                            return Response(data={'message': _("Ya existen actividades agendadas en esa fecha y hora")},
                                        status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        except Exception as err:
            print(err)
            return Response(data={'message': _("Ocurrió un error durante el proceso")},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)     