#!/usr/bin/env python
"""
DataNexus API Test Suite
Tests all functionality including CRUD APIs, weather integration, and data validation
"""

import requests
import json
import sys
from datetime import datetime

# Configuration
BASE_URL = "http://127.0.0.1:8003"
HEADERS = {'Content-Type': 'application/json'}

def test_response(response, test_name):
    """Helper function to test API responses"""
    try:
        if response.status_code in [200, 201]:
            print(f"✅ {test_name}: SUCCESS ({response.status_code})")
            return True, response.json() if response.content else {}
        else:
            print(f"❌ {test_name}: FAILED ({response.status_code}) - {response.text}")
            return False, {}
    except Exception as e:
        print(f"❌ {test_name}: ERROR - {str(e)}")
        return False, {}

def test_books_crud():
    """Test Books CRUD operations"""
    print("\n📚 Testing Books CRUD API...")
    
    # Test GET all books
    success, books = test_response(
        requests.get(f"{BASE_URL}/api/books/"),
        "GET /api/books/ (List all books)"
    )
    
    # Test POST create book
    book_data = {
        "title": "Test Book API",
        "author": "Test Author",
        "published_date": "2023-01-01",
        "description": "A test book for API validation"
    }
    
    success, created_book = test_response(
        requests.post(f"{BASE_URL}/api/books/", json=book_data, headers=HEADERS),
        "POST /api/books/ (Create book)"
    )
    
    if success and created_book:
        book_id = created_book.get('id')
        
        # Test GET specific book
        success, book = test_response(
            requests.get(f"{BASE_URL}/api/books/{book_id}/"),
            f"GET /api/books/{book_id}/ (Get specific book)"
        )
        
        # Test PUT update book
        updated_data = book_data.copy()
        updated_data['title'] = "Updated Test Book"
        
        success, updated_book = test_response(
            requests.put(f"{BASE_URL}/api/books/{book_id}/", json=updated_data, headers=HEADERS),
            f"PUT /api/books/{book_id}/ (Update book)"
        )
        
        # Test DELETE book
        success, _ = test_response(
            requests.delete(f"{BASE_URL}/api/books/{book_id}/"),
            f"DELETE /api/books/{book_id}/ (Delete book)"
        )
    
    return True

def test_weather_api():
    """Test Weather API integration"""
    print("\n🌤️ Testing Weather API Integration...")
    
    # Test GET weather data
    success, weather_data = test_response(
        requests.get(f"{BASE_URL}/api/external/weather/"),
        "GET /api/external/weather/ (List weather data)"
    )
    
    # Test fetch weather for city
    city_data = {"city": "Berlin", "country": "DE"}
    success, fetched_weather = test_response(
        requests.post(f"{BASE_URL}/api/external/weather/fetch/", json=city_data, headers=HEADERS),
        "POST /api/external/weather/fetch/ (Fetch weather)"
    )
    
    # Test latest weather
    success, latest_weather = test_response(
        requests.get(f"{BASE_URL}/api/external/weather/latest/"),
        "GET /api/external/weather/latest/ (Latest weather)"
    )
    
    # Test weather statistics
    success, stats = test_response(
        requests.get(f"{BASE_URL}/api/external/weather/stats/"),
        "GET /api/external/weather/stats/ (Weather statistics)"
    )
    
    return True

def test_web_pages():
    """Test web pages and dashboard"""
    print("\n🌐 Testing Web Pages...")
    
    # Test home page
    success, _ = test_response(
        requests.get(f"{BASE_URL}/"),
        "GET / (Home page)"
    )
    
    # Test dashboard
    success, _ = test_response(
        requests.get(f"{BASE_URL}/dashboard/"),
        "GET /dashboard/ (Dashboard page)"
    )
    
    # Test admin (should redirect to login)
    response = requests.get(f"{BASE_URL}/admin/")
    if response.status_code in [200, 302]:  # 302 is redirect to login
        print(f"✅ GET /admin/ (Admin page): SUCCESS ({response.status_code})")
    else:
        print(f"❌ GET /admin/ (Admin page): FAILED ({response.status_code})")
    
    return True

def test_data_integrity():
    """Test data integrity and relationships"""
    print("\n🔍 Testing Data Integrity...")
    
    # Get books count
    response = requests.get(f"{BASE_URL}/api/books/")
    if response.status_code == 200:
        books_count = len(response.json())
        print(f"✅ Books in database: {books_count}")
    
    # Get weather records count
    response = requests.get(f"{BASE_URL}/api/external/weather/")
    if response.status_code == 200:
        weather_count = len(response.json())
        print(f"✅ Weather records in database: {weather_count}")
    
    # Test weather statistics
    response = requests.get(f"{BASE_URL}/api/external/weather/stats/")
    if response.status_code == 200:
        stats = response.json()
        print(f"✅ Weather Statistics:")
        print(f"   - Total records: {stats.get('total_records', 0)}")
        print(f"   - Unique cities: {stats.get('unique_cities', 0)}")
        print(f"   - Average temperature: {stats.get('average_temperature', 'N/A')}°C")
    
    return True

def main():
    """Main test runner"""
    print("🚀 DataNexus API Test Suite")
    print("=" * 50)
    
    try:
        # Test server connectivity
        response = requests.get(BASE_URL, timeout=5)
        print(f"✅ Server is running at {BASE_URL}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to server at {BASE_URL}")
        print("Make sure Django server is running with: python manage.py runserver 8002")
        sys.exit(1)
    
    # Run all tests
    test_books_crud()
    test_weather_api()
    test_web_pages()
    test_data_integrity()
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed!")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()