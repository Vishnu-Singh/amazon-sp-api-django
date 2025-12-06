# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Docker and Docker Compose installed
- Amazon SP-API credentials (or use placeholders for testing)

### Steps

1. **Clone and navigate to the project:**
   ```bash
   git clone https://github.com/Vishnu-Singh/amazon-sp-api-django.git
   cd amazon-sp-api-django
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials (or leave as placeholders for testing)
   nano .env
   ```

3. **Start the services:**
   ```bash
   docker-compose up --build
   ```

4. **Access the API:**
   - Root endpoint: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/
   - API documentation in README.md

### Example API Calls

```bash
# Get API info
curl http://localhost:8000/

# Test Feeds API
curl "http://localhost:8000/api/feeds/?marketplaceIds=ATVPDKIKX0DER"

# Test Orders API
curl "http://localhost:8000/api/orders/?marketplaceIds=ATVPDKIKX0DER"

# Test Catalog API
curl "http://localhost:8000/api/catalog/?keywords=laptop&marketplaceIds=ATVPDKIKX0DER"
```

### Create Admin User

```bash
docker-compose exec web python manage.py createsuperuser
```

### View Logs

```bash
docker-compose logs -f web
```

### Stop Services

```bash
docker-compose down
```

## 📝 Next Steps

1. Configure your Amazon SP-API credentials in `.env`
2. Review the comprehensive README.md for detailed documentation
3. Customize the endpoints in each app's `views.py` as needed
4. Add your business logic and data models
5. Deploy to your preferred hosting platform

## 🔧 Development Mode (Without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and set USE_SQLITE=True and DB_HOST=localhost

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Access at: http://localhost:8000/

## 🆘 Troubleshooting

**Port already in use:**
```bash
docker-compose down
# Or change port in docker-compose.yml
```

**Database connection issues:**
```bash
docker-compose down -v
docker-compose up --build
```

**View detailed errors:**
```bash
docker-compose logs web
```

For more help, see the full README.md
