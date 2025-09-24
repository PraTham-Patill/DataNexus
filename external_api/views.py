from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.db import models
from .models import WeatherData
from .serializers import WeatherDataSerializer, CityWeatherRequestSerializer
from .services import get_weather_service

class WeatherDataListView(generics.ListAPIView):
    """
    List all weather data records
    """
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class WeatherDataDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific weather data record
    """
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

@api_view(['POST'])
def fetch_weather_data(request):
    """
    Fetch weather data from external API and store in database
    """
    serializer = CityWeatherRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        city = serializer.validated_data['city']
        country = serializer.validated_data.get('country')
        
        weather_service = get_weather_service()
        weather_data = weather_service.get_weather_by_city(city, country)
        
        if weather_data:
            # Save to database
            weather_record = WeatherData.objects.create(**weather_data)
            response_serializer = WeatherDataSerializer(weather_record)
            
            return Response({
                'message': 'Weather data fetched and saved successfully',
                'data': response_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Failed to fetch weather data'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_latest_weather(request):
    """
    Get the latest weather data for each city
    """
    # Get the latest record for each unique city
    latest_weather = WeatherData.objects.order_by('city', '-fetched_at').distinct('city')
    serializer = WeatherDataSerializer(latest_weather, many=True)
    
    return Response({
        'count': len(serializer.data),
        'data': serializer.data
    })

@api_view(['GET'])
def weather_statistics(request):
    """
    Get basic weather statistics
    """
    total_records = WeatherData.objects.count()
    unique_cities = WeatherData.objects.values('city').distinct().count()
    
    if total_records > 0:
        avg_temp = WeatherData.objects.aggregate(
            avg_temp=models.Avg('temperature')
        )['avg_temp']
        
        max_temp = WeatherData.objects.aggregate(
            max_temp=models.Max('temperature')
        )['max_temp']
        
        min_temp = WeatherData.objects.aggregate(
            min_temp=models.Min('temperature')
        )['min_temp']
    else:
        avg_temp = max_temp = min_temp = None
    
    return Response({
        'total_records': total_records,
        'unique_cities': unique_cities,
        'average_temperature': round(avg_temp, 2) if avg_temp else None,
        'max_temperature': max_temp,
        'min_temperature': min_temp
    })
