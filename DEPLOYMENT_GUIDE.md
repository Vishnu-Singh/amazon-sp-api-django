# Deployment Guide

This guide provides instructions for deploying the Amazon SP-API Django project to various platforms.

## Table of Contents

1. [Docker Deployment (Recommended)](#docker-deployment)
2. [Local Development](#local-development)
3. [Cloud Deployment](#cloud-deployment)
4. [Production Checklist](#production-checklist)

## Docker Deployment

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+
- Amazon SP-API credentials

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vishnu-Singh/amazon-sp-api-django.git
   cd amazon-sp-api-django
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   nano .env  # Edit with your credentials
   ```

3. **Start services:**
   ```bash
   docker-compose up -d --build
   ```

4. **Run migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create admin user:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application:**
   - API: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL 15+ (or use SQLite for testing)

### Steps

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   ```bash
   cp .env.example .env
   # For SQLite testing, set USE_SQLITE=True
   nano .env
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server:**
   ```bash
   python manage.py runserver
   ```

## Cloud Deployment

### AWS Elastic Beanstalk

1. **Install EB CLI:**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB application:**
   ```bash
   eb init -p python-3.11 amazon-sp-api
   ```

3. **Create environment:**
   ```bash
   eb create amazon-sp-api-env
   ```

4. **Configure environment variables:**
   ```bash
   eb setenv SECRET_KEY=your-secret-key \
            DEBUG=False \
            ALLOWED_HOSTS=your-domain.com \
            # ... add all other environment variables
   ```

5. **Deploy:**
   ```bash
   eb deploy
   ```

### Heroku

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   heroku create amazon-sp-api-app
   ```

3. **Add PostgreSQL:**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   # ... add all other environment variables
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   ```

6. **Run migrations:**
   ```bash
   heroku run python manage.py migrate
   ```

### Google Cloud Run

1. **Build and push Docker image:**
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/amazon-sp-api
   ```

2. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy amazon-sp-api \
     --image gcr.io/YOUR_PROJECT_ID/amazon-sp-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

3. **Set environment variables:**
   ```bash
   gcloud run services update amazon-sp-api \
     --update-env-vars SECRET_KEY=your-secret-key,DEBUG=False
   ```

### DigitalOcean App Platform

1. **Connect GitHub repository** in DigitalOcean dashboard

2. **Configure build settings:**
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Run Command: `gunicorn --bind 0.0.0.0:8080 amazon_sp_api.wsgi:application`

3. **Add PostgreSQL database** in DigitalOcean dashboard

4. **Configure environment variables** in the dashboard

5. **Deploy** from the dashboard

## Production Checklist

### Security
- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY` (50+ characters)
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Use HTTPS (configure SSL/TLS certificates)
- [ ] Enable HSTS, SECURE_SSL_REDIRECT
- [ ] Set SECURE_COOKIE_SECURE=True
- [ ] Set CSRF_COOKIE_SECURE=True
- [ ] Implement AWS Signature V4 authentication
- [ ] Use environment variables for all secrets
- [ ] Rotate credentials regularly

### Database
- [ ] Use PostgreSQL (not SQLite) in production
- [ ] Configure database backups
- [ ] Set up database connection pooling
- [ ] Optimize database indexes
- [ ] Configure database monitoring

### Performance
- [ ] Enable Django caching (Redis/Memcached)
- [ ] Configure static file serving (CDN)
- [ ] Set up load balancing
- [ ] Configure worker processes (3-5 per core)
- [ ] Enable gzip compression
- [ ] Optimize database queries

### Monitoring
- [ ] Set up application monitoring (New Relic, Datadog, etc.)
- [ ] Configure error tracking (Sentry, Rollbar)
- [ ] Set up log aggregation (CloudWatch, ELK Stack)
- [ ] Configure uptime monitoring
- [ ] Set up performance monitoring
- [ ] Configure alerts for critical errors

### Scaling
- [ ] Use managed database service
- [ ] Configure auto-scaling
- [ ] Set up caching layer
- [ ] Use CDN for static files
- [ ] Implement rate limiting
- [ ] Configure background job queue (Celery)

### Backup & Recovery
- [ ] Automated database backups
- [ ] Test restore procedures
- [ ] Document disaster recovery plan
- [ ] Configure point-in-time recovery
- [ ] Store backups in multiple locations

### Documentation
- [ ] Document deployment process
- [ ] Document environment variables
- [ ] Document API endpoints
- [ ] Create runbooks for common issues
- [ ] Document scaling procedures

## Environment Variables

Required environment variables for production:

```env
# Django Settings
SECRET_KEY=your-production-secret-key-50-chars-minimum
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# Database
DB_NAME=amazon_sp_api_db
DB_USER=your_db_user
DB_PASSWORD=your_secure_db_password
DB_HOST=your-db-host
DB_PORT=5432

# Amazon SP-API Credentials
AMAZON_SP_API_BASE_URL=https://sellingpartnerapi-na.amazon.com
AMAZON_SP_API_REFRESH_TOKEN=your_refresh_token
AMAZON_SP_API_CLIENT_ID=your_client_id
AMAZON_SP_API_CLIENT_SECRET=your_client_secret
AMAZON_SP_API_ACCESS_KEY=your_aws_access_key
AMAZON_SP_API_SECRET_KEY=your_aws_secret_key
AMAZON_SP_API_ROLE_ARN=arn:aws:iam::account:role/your-role
```

## Troubleshooting

### Common Issues

**Database connection errors:**
- Check database credentials
- Verify database host is accessible
- Ensure database exists and user has permissions

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**502 Bad Gateway:**
- Check application logs
- Verify Gunicorn is running
- Check worker timeouts

**Amazon SP-API authentication errors:**
- Verify credentials are correct
- Check refresh token validity
- Ensure AWS IAM permissions are set correctly

## Support

For deployment issues:
- Check logs: `docker-compose logs web`
- Review Django logs
- Check database connectivity
- Verify environment variables

For Amazon SP-API issues:
- Consult [SP-API documentation](https://developer-docs.amazon.com/sp-api/)
- Verify credentials and permissions
- Check API rate limits

## Maintenance

### Regular Tasks

**Weekly:**
- Review application logs
- Check error rates
- Monitor performance metrics

**Monthly:**
- Update dependencies
- Review security advisories
- Rotate access credentials
- Test backup restoration

**Quarterly:**
- Review and update documentation
- Performance optimization review
- Security audit
- Disaster recovery drill
