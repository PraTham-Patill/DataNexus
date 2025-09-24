from django.db import models
from django.utils import timezone

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    temperature = models.FloatField(default=0.0)  # in Celsius
    feels_like = models.FloatField(default=0.0)
    humidity = models.IntegerField(default=50)
    pressure = models.IntegerField(default=1013)
    description = models.CharField(max_length=200, default='Clear sky')
    wind_speed = models.FloatField(default=0.0)
    visibility = models.IntegerField(null=True, blank=True)
    fetched_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-fetched_at']
        
    def __str__(self):
        return f"{self.city}, {self.country} - {self.temperature}°C"
