from django.urls import path
from . import views

app_name = 'external_api'

urlpatterns = [
    path('weather/', views.WeatherDataListView.as_view(), name='weather-list'),
    path('weather/<int:pk>/', views.WeatherDataDetailView.as_view(), name='weather-detail'),
    path('weather/fetch/', views.fetch_weather_data, name='fetch-weather'),
    path('weather/latest/', views.get_latest_weather, name='latest-weather'),
    path('weather/stats/', views.weather_statistics, name='weather-stats'),
]