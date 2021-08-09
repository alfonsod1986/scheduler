from rest_framework import serializers
from scheduler.apps.schedule.models import Property, Activity, Survey
from ..functions import get_conditional_status

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class PropertyCustomizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'address']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class ActivityListSerializer(serializers.ModelSerializer):
    condition = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        exclude = ('updated_at',)

    def get_condition(self, obj):
        return get_conditional_status(obj.schedule, obj.status)
    
    def to_representation(self, instance):
        representation = super(ActivityListSerializer, self).to_representation(instance)
        representation['property_id'] = PropertyCustomizedSerializer(instance.property_id, context={'request': self.context.get('request')}).data
        return representation