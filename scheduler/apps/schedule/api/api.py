from datetime import datetime
from django.db.models import Q
from rest_framework import viewsets, status
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from scheduler.apps.schedule.models import Property, Activity
from rest_framework.response import Response
from ..constants import ENABLED, DISABLED, UTC_TZ, NOW_AFTER_TWO_WEEKS_ON_DAYS, NOW_BEFORE_THREE_DAYS
from ..functions import is_activity_lasts_a_maximum_one_hour, get_custom_now
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
    page_size = 10
    max_page_size = 1000

    def list(self, request):
        try:
            start_date = request.GET.get('start_date', None) 
            end_date = request.GET.get('end_date', None)

            start_date = start_date if start_date is not None else get_custom_now(NOW_BEFORE_THREE_DAYS)
            end_date = end_date if end_date is not None else get_custom_now(NOW_AFTER_TWO_WEEKS_ON_DAYS)


            activities = Activity.objects.filter(
                schedule__date__gte=start_date, schedule__date__lte=end_date).filter(~Q(status=DISABLED)).order_by('schedule')

            page = self.paginator.paginate_queryset(activities, request)

            serializer = ActivityListSerializer(page, many=True)
            return self.paginator.get_paginated_response(serializer.data)

        except Exception as err:
            print(err)
            return Response(data={'message': _("Ocurrió un error durante el proceso")},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            activity = Activity.objects.get(pk=pk)
            serializer = ActivityListSerializer(activity)
            return Response(data=serializer.data,
                                        status=status.HTTP_200_OK)
        except Activity.DoesNotExist:
            return Response(data={'message': _("La actividad que intentas consultar no existe")},
                                        status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(data={'message': _("Ocurrió un error durante el proceso")},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                property_id = request.data.get('property_id')
                schedule = request.data.get('schedule')
                schedule_datetime = UTC_TZ.localize(datetime.strptime(schedule, '%Y-%m-%dT%H:%M:%S.%fZ'))
                schedule_date = schedule[:10]
                prop = Property.objects.get(pk=property_id)

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
    
    def update(self, request, pk=None):
        try:
            schedule = request.data.get('schedule', None)
            if not schedule:
                return Response(data={'message': _("Debes de mandar la fecha y hora para poder reagendar la actividad")},
                                        status=status.HTTP_400_BAD_REQUEST)
            schedule_datetime = UTC_TZ.localize(datetime.strptime(schedule, '%Y-%m-%dT%H:%M:%S.%fZ'))
            schedule_date = schedule[:10]

            activity = Activity.objects.get(pk=pk)

            activities = Activity.objects.filter(
                property_id=activity.property_id, schedule__date=schedule_date).filter(~Q(id=pk)).order_by('schedule')
            
            if activities:
                for activity in activities:
                    if schedule_datetime > activity.schedule:
                        if not is_activity_lasts_a_maximum_one_hour(activity.schedule, schedule_datetime):
                            return Response(data={'message': _("La actividad debe durar 1 hora como máximo")},
                                        status=status.HTTP_400_BAD_REQUEST)
                    if activity.schedule == schedule_datetime:
                        return Response(data={'message': _("Ya existen actividades agendadas en esa fecha y hora")},
                                        status=status.HTTP_400_BAD_REQUEST)
            
            activity.schedule =schedule_datetime
            activity.save()

            return Response(data={'message': _("La actividad ha sido reagendada correctamente")},
                                        status=status.HTTP_200_OK)
        except Activity.DoesNotExist:
            return Response(data={'message': _("La actividad que intentas reprogramar no existe o está cancelada")},
                                        status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(data={'message': _("Ocurrió un error durante el proceso")},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs['partial'] = True
            return self.update(request, *args, **kwargs)
        except Exception as err:
            print(err)
            return Response(data={'message': _("Ocurrió un error durante el proceso")},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            activity = Activity.objects.get(pk=pk)
            activity.status = DISABLED
            activity.save()
            return Response(data={'message': _("La actividad se ha cancelado")},
                                        status=status.HTTP_204_NO_CONTENT)
        except Activity.DoesNotExist:
            return Response(data={'message': _("La actividad que intentas cancelar no existe")},
                                        status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(data={'message': _("Ocurrió un error durante el proceso")},
                                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
