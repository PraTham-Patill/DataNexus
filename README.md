# DataNexus 🚀

A comprehensive data management and visualization platform built with Django REST Framework. DataNexus combines powerful REST APIs, third-party integrations, and interactive data visualizations in a modern web application.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.7-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **📚 Book Management**: Complete CRUD REST API for book collection management
- **🌤️ Weather Integration**: Real-time weather data fetching from OpenWeather API
- **📊 Data Visualization**: Interactive charts using Chart.js and Plotly
- **🎨 Modern UI**: Responsive Bootstrap-based interface
- **🔒 Admin Interface**: Django admin for data management
- **🚀 Production Ready**: Configured for Railway/Render deployment
- **📱 API Documentation**: Well-documented REST endpoints

## 🏗️ Project Structure

```
DataNexus/
├── books/                  # Book management app
│   ├── models.py          # Book model
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   └── urls.py            # URL routing
├── external_api/          # Weather API integration
│   ├── models.py          # Weather data model
│   ├── services.py        # Weather service layer
│   ├── serializers.py     # API serializers
│   └── views.py           # Weather API views
├── dashboard/             # Data visualization
│   ├── views.py           # Dashboard views
│   └── urls.py            # Dashboard routing
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Home page
│   └── dashboard.html     # Dashboard with charts
├── datanexus/            # Main project settings
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
└── README.md             # This file
```

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7, Django REST Framework 3.14.0
- **Database**: SQLite (dev), PostgreSQL (production)
- **Frontend**: HTML5, Bootstrap 5, Chart.js, Plotly.js
- **External APIs**: OpenWeather API
- **Deployment**: Railway, Render (with Gunicorn + WhiteNoise)
- **Environment**: Python 3.10+

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd DataNexus
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env with your settings (optional for development)
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional)**
   ```bash
   python manage.py shell -c "
   from books.models import Book
   from external_api.services import get_weather_service
   from external_api.models import WeatherData
   from datetime import date
   
   # Create sample books
   Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald', published_date=date(1925, 4, 10))
   Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', published_date=date(1960, 7, 11))
   
   # Create sample weather data
   weather_service = get_weather_service()
   cities = [('New York', 'US'), ('London', 'GB'), ('Tokyo', 'JP')]
   for city, country in cities:
       weather_data = weather_service.get_weather_by_city(city, country)
       WeatherData.objects.create(**weather_data)
   "
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Home: http://127.0.0.1:8000/
   - Dashboard: http://127.0.0.1:8000/dashboard/
   - Admin: http://127.0.0.1:8000/admin/
   - API Root: http://127.0.0.1:8000/api/

## 📖 API Documentation

### Books API

| Endpoint | Method | Description | Request Body |
|----------|--------|-------------|--------------|
| `/api/books/` | GET | List all books | - |
| `/api/books/` | POST | Create new book | `{"title": "...", "author": "...", "published_date": "YYYY-MM-DD", "description": "..."}` |
| `/api/books/{id}/` | GET | Get specific book | - |
| `/api/books/{id}/` | PUT | Update book | `{"title": "...", "author": "...", "published_date": "YYYY-MM-DD", "description": "..."}` |
| `/api/books/{id}/` | DELETE | Delete book | - |

### Weather API

| Endpoint | Method | Description | Request Body |
|----------|--------|-------------|--------------|
| `/api/external/weather/` | GET | List all weather records | - |
| `/api/external/weather/fetch/` | POST | Fetch weather for city | `{"city": "London", "country": "GB"}` |
| `/api/external/weather/latest/` | GET | Latest weather per city | - |
| `/api/external/weather/stats/` | GET | Weather statistics | - |
| `/api/external/weather/{id}/` | GET | Get specific weather record | - |

### API Examples

**Create a new book:**
```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "1984",
    "author": "George Orwell",
    "published_date": "1949-06-08",
    "description": "A dystopian social science fiction novel"
  }'
```

**Fetch weather data:**
```bash
curl -X POST http://127.0.0.1:8000/api/external/weather/fetch/ \
  -H "Content-Type: application/json" \
  -d '{
    "city": "Paris",
    "country": "FR"
  }'
```

**Get all books:**
```bash
curl http://127.0.0.1:8000/api/books/
```

## 📊 Data Visualization

The dashboard provides interactive visualizations:

- **Temperature Bar Chart**: Shows temperature data by city using Chart.js
- **Humidity Pie Chart**: Displays humidity distribution across cities
- **Plotly Chart**: Advanced visualization comparing temperature and humidity
- **Data Table**: Responsive table showing latest weather records

Access the dashboard at `/dashboard/` to explore your data visually.

## 🚀 Deployment

### Railway Deployment

1. **Prepare for deployment**
   ```bash
   # Ensure all dependencies are in requirements.txt
   pip freeze > requirements.txt
   ```

2. **Create Railway project**
   - Go to [Railway](https://railway.app)
   - Connect your GitHub repository
   - Deploy from main branch

3. **Set environment variables**
   ```
   SECRET_KEY=your-production-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app.railway.app
   DATABASE_URL=postgresql://... (provided by Railway)
   OPENWEATHER_API_KEY=your-api-key
   ```

4. **Deploy**
   - Railway will automatically build and deploy
   - Run migrations: `python manage.py migrate`
   - Create superuser: `python manage.py createsuperuser`

### Render Deployment

1. **Create Render account** at [render.com](https://render.com)

2. **Create new Web Service**
   - Connect your GitHub repository
   - Use these settings:
     - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
     - **Start Command**: `gunicorn datanexus.wsgi:application`

3. **Set environment variables** (same as Railway)

4. **Deploy** - Render will handle the rest

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SECRET_KEY` | Django secret key | Yes | - |
| `DEBUG` | Debug mode | No | `True` |
| `ALLOWED_HOSTS` | Allowed hosts (comma-separated) | Yes | `localhost,127.0.0.1` |
| `DATABASE_URL` | PostgreSQL database URL | No | SQLite |
| `OPENWEATHER_API_KEY` | OpenWeather API key | No | Mock data |

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Test specific apps:
```bash
python manage.py test books
python manage.py test external_api
```

## 📁 Static Files

Static files are handled by WhiteNoise in production:
- CSS, JS, and images are served efficiently
- Files are compressed and cached
- No need for external CDN setup

## 🔧 Configuration

### OpenWeather API Setup

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Set `OPENWEATHER_API_KEY` in your environment
4. Without API key, mock data will be used

### Database Configuration

**Development**: SQLite (included)
**Production**: PostgreSQL (recommended)

For PostgreSQL, set `DATABASE_URL`:
```
DATABASE_URL=postgresql://user:password@host:port/database
```

## 🐛 Troubleshooting

### Common Issues

1. **Migration errors**
   ```bash
   python manage.py makemigrations --empty appname
   python manage.py migrate
   ```

2. **Static files not loading**
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Database connection issues**
   - Check `DATABASE_URL` format
   - Ensure PostgreSQL is running
   - Verify credentials

4. **API key issues**
   - Verify `OPENWEATHER_API_KEY` is set
   - Check API key validity
   - Mock service will work without key

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Enhancements

- [ ] User authentication and authorization
- [ ] More third-party API integrations
- [ ] Advanced data analytics
- [ ] Real-time data updates with WebSockets
- [ ] Mobile app development
- [ ] Docker containerization
- [ ] Comprehensive test coverage
- [ ] API rate limiting and caching

## 📞 Support

For support, email support@datanexus.com or create an issue in the repository.

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Built with ❤️ using Django and modern web technologies**