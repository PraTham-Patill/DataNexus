# DataNexus 🚀

**DataNexus** is a Django web application demonstrating CRUD REST APIs, third-party API integration, and interactive data visualization. It uses **Django REST Framework** with **PostgreSQL** for production.

---

## 🌟 Key Features

* **Book Management**: Full CRUD REST API
* **Weather Integration**: Fetch real-time data from OpenWeather API
* **Data Visualization**: Interactive charts with Chart.js and Plotly
* **Responsive UI**: Bootstrap-based modern interface
* **Admin Panel**: Manage books and weather data
* **Deployment Ready**: Configured for Railway/Render

---

## 🏏️ Project Structure

```
DataNexus/
├── books/                  # CRUD API for books
├── external_api/           # Weather API integration
├── dashboard/              # Interactive charts
├── templates/              # HTML templates
├── datanexus/              # Django settings
├── requirements.txt        # Dependencies
├── Procfile                # Deployment config
├── runtime.txt             # Python version
└── README.md               # Project documentation
```

---

## 🛠️ Technology Stack

* **Backend**: Django 4.2.7, Django REST Framework 3.14.0
* **Database**: SQLite (dev), PostgreSQL (prod)
* **Frontend**: Bootstrap 5, Chart.js, Plotly.js
* **Deployment**: Railway, Render
* **Python**: 3.10+

---

## 🚀 Setup (Local)

1. Clone the repository:

```bash
git clone https://github.com/PraTham-Patill/DataNexus.git
cd DataNexus
```

2. Create a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Setup environment variables:

```bash
cp .env.example .env
# Edit if needed (SECRET_KEY, DEBUG, DATABASE_URL, OPENWEATHER_API_KEY)
```

5. Run migrations and create superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the application:

* Home: `http://127.0.0.1:8000/`
* Dashboard: `http://127.0.0.1:8000/dashboard/`
* Admin: `http://127.0.0.1:8000/admin/`
* Books API: `http://127.0.0.1:8000/api/books/`
* Weather API: `http://127.0.0.1:8000/api/external/weather/`

---

## 📜 API Endpoints

### Books API

| Endpoint           | Method         | Description                        |
| ------------------ | -------------- | ---------------------------------- |
| `/api/books/`      | GET/POST       | List or create books               |
| `/api/books/{id}/` | GET/PUT/DELETE | Retrieve, update, or delete a book |

### Weather API

| Endpoint                        | Method | Description              |
| ------------------------------- | ------ | ------------------------ |
| `/api/external/weather/`        | GET    | List all weather records |
| `/api/external/weather/fetch/`  | POST   | Fetch weather for a city |
| `/api/external/weather/latest/` | GET    | Latest weather per city  |
| `/api/external/weather/stats/`  | GET    | Weather statistics       |

---

## 📊 Data Visualization

* **Temperature Bar Chart** (Chart.js)
* **Humidity Pie Chart** (Chart.js)
* **Interactive Plotly charts** comparing temperature and humidity
* Responsive dashboard for desktop and mobile

---

## ⚙️ Deployment

### Railway Deployment

1. Connect GitHub repository
2. Add PostgreSQL database
3. Set environment variables:

```
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.railway.app
DATABASE_URL=postgresql://user:password@host:port/database
OPENWEATHER_API_KEY=your-api-key
```

4. Deploy and run migrations
5. Create superuser

### Render Deployment

1. Connect GitHub repository
2. Build command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

3. Start command:

```bash
gunicorn datanexus.wsgi:application
```

4. Set same environment variables as above
5. Deploy

---

## 🤝 Testing

Run tests:

```bash
python manage.py test
```

Test specific apps:

```bash
python manage.py test books
python manage.py test external_api
```

---


This project meets all the requirements: CRUD REST API, third-party API integration, data visualization, and deployment-ready configuration.
