from rest_framework import serializers
from .models import TouristDestination

class TouristDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristDestination
        fields = '__all__'
