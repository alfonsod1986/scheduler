from django_filters import rest_framework as filters
from scheduler.apps.schedule.models import Property, Activity

class PropertyFilter(filters.FilterSet):

    class Meta:
        model = Property
        fields = {'id', 'title', 'status'}