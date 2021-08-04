from django_filters import rest_framework as filters
from scheduler.apps.schedule.models import Property

class PropertyFilter(filters.FilterSet):

    class Meta:
        model = Property
        fields = {'id', 'title', 'status'}