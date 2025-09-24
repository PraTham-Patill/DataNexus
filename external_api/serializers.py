from rest_framework import serializers
from .models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
        
class CityWeatherRequestSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100, required=False)