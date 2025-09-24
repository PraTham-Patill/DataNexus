from django.shortcuts import render
from django.http import JsonResponse
from books.models import Book
from external_api.models import WeatherData

def home(request):
    """
    Home page with basic project information
    """
    context = {
        'project_name': 'DataNexus',
        'total_books': Book.objects.count(),
        'total_weather_records': WeatherData.objects.count(),
    }
    return render(request, 'home.html', context)

def dashboard(request):
    """
    Dashboard with data visualization
    """
    # Get data for charts
    book_count = Book.objects.count()
    weather_count = WeatherData.objects.count()
    
    # Get weather data for chart
    weather_data = WeatherData.objects.all()[:10]  # Latest 10 records
    
    context = {
        'book_count': book_count,
        'weather_count': weather_count,
        'weather_data': weather_data,
    }
    return render(request, 'dashboard.html', context)
