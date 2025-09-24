import requests
from django.conf import settings
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


class OpenWeatherService:
    """
    Service to interact with OpenWeather API
    """
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        if not self.api_key:
            logger.warning("OpenWeather API key not configured")
    
    def get_weather_by_city(self, city: str, country_code: str = None) -> Optional[Dict]:
        """
        Fetch weather data for a specific city
        
        Args:
            city: City name
            country_code: Optional country code (e.g., 'US', 'GB')
            
        Returns:
            Dictionary with weather data or None if failed
        """
        if not self.api_key:
            logger.error("OpenWeather API key not configured")
            return None
        
        try:
            # Prepare query parameter
            query = city
            if country_code:
                query = f"{city},{country_code}"
            
            params = {
                'q': query,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Transform the data to match our model
            return self._transform_weather_data(data)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data for {city}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching weather data for {city}: {e}")
            return None
    
    def get_weather_by_coordinates(self, lat: float, lon: float) -> Optional[Dict]:
        """
        Fetch weather data for specific coordinates
        
        Args:
            lat: Latitude
            lon: Longitude
            
        Returns:
            Dictionary with weather data or None if failed
        """
        if not self.api_key:
            logger.error("OpenWeather API key not configured")
            return None
        
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius
            }
            
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Transform the data to match our model
            return self._transform_weather_data(data)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data for coordinates {lat}, {lon}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching weather data for coordinates {lat}, {lon}: {e}")
            return None
    
    def _transform_weather_data(self, api_data: Dict) -> Dict:
        """
        Transform OpenWeather API response to our model format
        
        Args:
            api_data: Raw API response data
            
        Returns:
            Transformed data dictionary
        """
        try:
            weather = api_data.get('weather', [{}])[0]
            main = api_data.get('main', {})
            wind = api_data.get('wind', {})
            sys = api_data.get('sys', {})
            
            return {
                'city': api_data.get('name', ''),
                'country': sys.get('country', ''),
                'temperature': main.get('temp', 0),
                'feels_like': main.get('feels_like', 0),
                'humidity': main.get('humidity', 0),
                'pressure': main.get('pressure', 0),
                'description': weather.get('description', ''),
                'wind_speed': wind.get('speed', 0),
                'visibility': api_data.get('visibility'),
            }
        except Exception as e:
            logger.error(f"Error transforming weather data: {e}")
            raise


# Mock service for testing without API key
class MockWeatherService:
    """
    Mock weather service for testing and demo purposes
    """
    
    def get_weather_by_city(self, city: str, country_code: str = None) -> Dict:
        """
        Return mock weather data
        """
        import random
        
        return {
            'city': city,
            'country': country_code or 'US',
            'temperature': round(random.uniform(-10, 35), 1),
            'feels_like': round(random.uniform(-10, 35), 1),
            'humidity': random.randint(30, 90),
            'pressure': random.randint(990, 1030),
            'description': random.choice([
                'clear sky', 'few clouds', 'scattered clouds',
                'broken clouds', 'light rain', 'moderate rain'
            ]),
            'wind_speed': round(random.uniform(0, 15), 1),
            'visibility': random.randint(5000, 10000),
        }
    
    def get_weather_by_coordinates(self, lat: float, lon: float) -> Dict:
        """
        Return mock weather data for coordinates
        """
        return self.get_weather_by_city("MockCity")


def get_weather_service():
    """
    Factory function to get appropriate weather service
    """
    if settings.OPENWEATHER_API_KEY:
        return OpenWeatherService()
    else:
        logger.info("Using mock weather service (no API key configured)")
        return MockWeatherService()