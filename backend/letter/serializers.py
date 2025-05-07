from rest_framework import serializers
from .models import Letter, LetterTracking

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'

class LetterTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LetterTracking
        fields = '__all__'
