from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'temperature', 'humidity', 'description', 'fetched_at')
    list_filter = ('country', 'fetched_at')
    search_fields = ('city', 'country', 'description')
    readonly_fields = ('fetched_at',)
    ordering = ('-fetched_at',)
