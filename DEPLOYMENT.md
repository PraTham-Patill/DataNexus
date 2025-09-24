# 🚀 DataNexus Deployment Guide

## Railway Deployment (Recommended)

### Prerequisites
1. GitHub account with your DataNexus repository
2. Railway account (https://railway.app)
3. Generate a new secret key for production

### Step 1: Generate Production Secret Key
```bash
python generate_secret_key.py
```
Copy the generated key for use in environment variables.

### Step 2: Deploy to Railway

1. **Sign up to Railway**
   - Go to https://railway.app
   - Sign up with your GitHub account

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your DataNexus repository

3. **Configure Environment Variables**
   Go to your project settings and add these variables:
   ```
   SECRET_KEY=your-generated-secret-key-from-step-1
   DEBUG=False
   ALLOWED_HOSTS=*.railway.app
   OPENWEATHER_API_KEY=your-api-key-optional
   ```

4. **Railway will automatically:**
   - Detect it's a Django app
   - Install dependencies from requirements.txt
   - Run migrations
   - Start the server with Gunicorn

5. **Add PostgreSQL Database**
   - In Railway dashboard, click "Add Plugin"
   - Select "PostgreSQL"
   - Railway will automatically set DATABASE_URL environment variable

6. **Deploy and Test**
   - Your app will be available at: `https://your-app-name.railway.app`
   - Check the deployment logs for any issues

### Step 3: Post-Deployment Setup

1. **Create Superuser**
   In Railway dashboard, go to your service and run:
   ```bash
   python manage.py createsuperuser
   ```

2. **Load Sample Data** (Optional)
   ```bash
   python manage.py shell -c "
   from books.models import Book
   from external_api.services import get_weather_service
   from external_api.models import WeatherData
   from datetime import date
   
   # Create sample books
   Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald', published_date=date(1925, 4, 10))
   Book.objects.create(title='1984', author='George Orwell', published_date=date(1949, 6, 8))
   
   # Create sample weather data
   weather_service = get_weather_service()
   cities = [('New York', 'US'), ('London', 'GB'), ('Tokyo', 'JP')]
   for city, country in cities:
       weather_data = weather_service.get_weather_by_city(city, country)
       WeatherData.objects.create(**weather_data)
   "
   ```

## Alternative: Render Deployment

### Step 1: Deploy to Render

1. **Sign up to Render**
   - Go to https://render.com
   - Sign up with your GitHub account

2. **Create Web Service**
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
     - **Start Command**: `gunicorn datanexus.wsgi:application`

3. **Environment Variables**
   Add the same variables as Railway:
   ```
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=*.onrender.com
   OPENWEATHER_API_KEY=your-api-key-optional
   ```

4. **Add PostgreSQL Database**
   - Create a PostgreSQL service in Render
   - Copy the internal database URL to your web service's DATABASE_URL

## Testing Your Deployment

### 1. Basic Functionality Test
- Homepage: `https://your-app.railway.app/`
- Dashboard: `https://your-app.railway.app/dashboard/`
- Admin: `https://your-app.railway.app/admin/`

### 2. API Endpoints Test
```bash
# Test Books API
curl https://your-app.railway.app/api/books/

# Test Weather API
curl https://your-app.railway.app/api/external/weather/

# Create a book
curl -X POST https://your-app.railway.app/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Book", "author": "Test Author", "published_date": "2023-01-01", "description": "Test"}'

# Fetch weather data
curl -X POST https://your-app.railway.app/api/external/weather/fetch/ \
  -H "Content-Type: application/json" \
  -d '{"city": "Berlin", "country": "DE"}'
```

### 3. Dashboard Visualization Test
- Visit `https://your-app.railway.app/dashboard/`
- Verify charts are loading with data
- Check that data tables show records

## Troubleshooting

### Common Issues

1. **Static files not loading**
   - Ensure `python manage.py collectstatic` runs in build command
   - Check STATIC_ROOT and STATICFILES_STORAGE settings

2. **Database connection issues**
   - Verify DATABASE_URL is set correctly
   - Ensure migrations run: `python manage.py migrate`

3. **Environment variables**
   - Double-check all required variables are set
   - Restart the service after changing variables

4. **Application errors**
   - Check deployment logs in Railway/Render dashboard
   - Enable DEBUG temporarily to see detailed errors

### Success Indicators

✅ Homepage loads without errors  
✅ Dashboard shows charts with data  
✅ Admin interface is accessible  
✅ API endpoints return data  
✅ Database operations work  
✅ Static files serve correctly  

## Security Notes

- Never commit `.env` files to Git
- Use strong, unique SECRET_KEY for production
- Keep DEBUG=False in production
- Regularly update dependencies
- Monitor your deployment logs

## Performance Optimization

- Static files are served by WhiteNoise
- Database queries are optimized with select_related
- Use CDN for external JavaScript libraries
- Enable database connection pooling if needed

Your DataNexus application is now production-ready! 🎉