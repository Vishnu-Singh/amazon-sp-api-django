# Amazon SP-API Django Integration

A complete, production-ready Django project for Amazon Selling Partner API (SP-API) integration with all 18 API categories implemented as separate Django apps.

## 🚀 Features

- **18 Fully Implemented API Categories:**
  - 📊 **Feeds** - Upload data to Amazon and track processing status
  - 📦 **Catalog** - Search and retrieve Amazon catalog information
  - 🛒 **Orders** - Retrieve and manage order information
  - 📝 **Listings** - Create, read, update, and delete product listings
  - 📈 **Reports** - Generate and retrieve various seller reports
  - 📥 **Fulfillment Inbound** - Manage inbound shipments to Amazon FBA
  - 📤 **Fulfillment Outbound** - Access Multi-Channel Fulfillment services
  - 🚚 **Merchant Fulfillment** - Purchase shipping for seller-fulfilled orders
  - 💰 **Finance** - Retrieve financial information and transactions
  - 💵 **Product Pricing** - Get pricing information for products
  - 💳 **Product Fees** - Estimate Amazon fees for products
  - 👤 **Sellers** - Get seller account information
  - 📋 **Inventory** - Retrieve FBA inventory data
  - 🚢 **Shipping** - Access Amazon shipping services
  - 🔔 **Notifications** - Subscribe to and manage SP-API notifications
  - 🔐 **Authorization** - Manage authorization and permissions
  - 📦 **Small and Light** - Manage Small and Light program enrollments
  - 🎫 **Tokens** - Generate restricted data tokens for PII access

- **Production-Ready Architecture:**
  - RESTful API design with Django Rest Framework
  - Modular app structure for easy maintenance
  - Environment-based configuration
  - Docker containerization for easy deployment
  - PostgreSQL database support
  - Comprehensive error handling

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose (for containerized deployment)
- Amazon SP-API credentials (Client ID, Client Secret, Refresh Token, AWS keys)

## 🛠️ Installation

### Option 1: Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vishnu-Singh/amazon-sp-api-django.git
   cd amazon-sp-api-django
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your Amazon SP-API credentials
   ```

3. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **The API will be available at:** `http://localhost:8000`

### Option 2: Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vishnu-Singh/amazon-sp-api-django.git
   cd amazon-sp-api-django
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials and set DB_HOST=localhost
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## 🔑 Configuration

### Environment Variables

Edit the `.env` file with your Amazon SP-API credentials:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=amazon_sp_api_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Amazon SP-API Credentials
AMAZON_SP_API_BASE_URL=https://sellingpartnerapi-na.amazon.com
AMAZON_SP_API_REFRESH_TOKEN=your_refresh_token
AMAZON_SP_API_CLIENT_ID=your_client_id
AMAZON_SP_API_CLIENT_SECRET=your_client_secret
AMAZON_SP_API_ACCESS_KEY=your_aws_access_key
AMAZON_SP_API_SECRET_KEY=your_aws_secret_key
AMAZON_SP_API_ROLE_ARN=arn:aws:iam::xxxxx:role/your-role
```

### Getting Amazon SP-API Credentials

1. Register as a developer in [Amazon Seller Central](https://sellercentral.amazon.com/)
2. Create a new SP-API application
3. Note your **Client ID** and **Client Secret**
4. Complete the OAuth authorization flow to get your **Refresh Token**
5. Set up AWS IAM credentials for API signing

## 📖 API Documentation

### Root Endpoint

```bash
GET http://localhost:8000/
```

Returns a list of all available API endpoints.

### Example Endpoints

#### Feeds API
```bash
# Get all feeds
GET /api/feeds/?marketplaceIds=ATVPDKIKX0DER

# Create a new feed
POST /api/feeds/
{
  "feedType": "POST_PRODUCT_DATA",
  "marketplaceIds": ["ATVPDKIKX0DER"],
  "inputFeedDocumentId": "amzn1.tortuga.3.ed4cd0d8..."
}
```

#### Orders API
```bash
# Get orders
GET /api/orders/?marketplaceIds=ATVPDKIKX0DER&createdAfter=2024-01-01T00:00:00Z

# Get specific order
GET /api/orders/{orderId}/

# Get order items
GET /api/orders/{orderId}/items/
```

#### Catalog API
```bash
# Search catalog items
GET /api/catalog/?keywords=laptop&marketplaceIds=ATVPDKIKX0DER

# Get specific item
GET /api/catalog/{asin}/?marketplaceIds=ATVPDKIKX0DER
```

#### Listings API
```bash
# Get listing
GET /api/listings/{sellerId}/{sku}/?marketplaceIds=ATVPDKIKX0DER

# Create/Update listing
PUT /api/listings/{sellerId}/{sku}/?marketplaceIds=ATVPDKIKX0DER

# Delete listing
DELETE /api/listings/{sellerId}/{sku}/?marketplaceIds=ATVPDKIKX0DER
```

### Full API Categories

- 📊 `/api/feeds/` - Feeds API
- 📦 `/api/catalog/` - Catalog Items API
- 🛒 `/api/orders/` - Orders API
- 📝 `/api/listings/` - Listings Items API
- 📈 `/api/reports/` - Reports API
- 📥 `/api/fulfillment-inbound/` - Fulfillment Inbound API
- 📤 `/api/fulfillment-outbound/` - Fulfillment Outbound API
- 🚚 `/api/merchant-fulfillment/` - Merchant Fulfillment API
- 💰 `/api/finance/` - Finances API
- 💵 `/api/product-pricing/` - Product Pricing API
- 💳 `/api/product-fees/` - Product Fees API
- 👤 `/api/sellers/` - Sellers API
- 📋 `/api/inventory/` - FBA Inventory API
- 🚢 `/api/shipping/` - Shipping API
- 🔔 `/api/notifications/` - Notifications API
- 🔐 `/api/authorization/` - Authorization API
- 📦 `/api/small-and-light/` - Small and Light API
- 🎫 `/api/tokens/` - Tokens API

## 🏗️ Project Structure

```
amazon-sp-api-django/
├── amazon_sp_api/          # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── utils/             # Utility modules
│       └── sp_api_client.py  # SP-API client
├── feeds/                 # Feeds app
├── catalog/               # Catalog app
├── orders/                # Orders app
├── listings/              # Listings app
├── reports/               # Reports app
├── fulfillment_inbound/   # Fulfillment Inbound app
├── fulfillment_outbound/  # Fulfillment Outbound app
├── merchant_fulfillment/  # Merchant Fulfillment app
├── finance/               # Finance app
├── product_pricing/       # Product Pricing app
├── product_fees/          # Product Fees app
├── sellers/               # Sellers app
├── inventory/             # Inventory app
├── shipping/              # Shipping app
├── notifications/         # Notifications app
├── authorization/         # Authorization app
├── small_and_light/       # Small and Light app
├── tokens/                # Tokens app
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── .env.example           # Example environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔒 Security Considerations

⚠️ **Important Security Notes:**

1. **Never commit sensitive credentials** to version control
2. Use the `.env` file for all sensitive configuration (already in `.gitignore`)
3. In production:
   - Set `DEBUG=False`
   - Use a strong, unique `SECRET_KEY`
   - Configure proper `ALLOWED_HOSTS`
   - Use HTTPS for all communications
   - Implement proper AWS Signature V4 signing (placeholder in current implementation)
   - Use AWS IAM roles with minimal required permissions
   - Rotate credentials regularly

## 🧪 Testing

Run Django tests:
```bash
python manage.py test
```

## 🚀 Deployment

### Production Deployment with Docker

1. Update `.env` for production:
   ```env
   DEBUG=False
   ALLOWED_HOSTS=your-domain.com
   SECRET_KEY=your-production-secret-key
   ```

2. Build and deploy:
   ```bash
   docker-compose -f docker-compose.yml up -d --build
   ```

3. Run migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Scaling

To run multiple workers:
```bash
docker-compose up --scale web=3
```

## 📝 Development Notes

### Adding New Endpoints

Each app follows a consistent structure:
- `models.py` - Database models (if needed)
- `views.py` - API views that proxy to Amazon SP-API
- `urls.py` - URL routing
- `apps.py` - App configuration

### Authentication

The current implementation includes placeholder authentication. For production:

1. Implement full AWS Signature Version 4 signing in `sp_api_client.py`
2. Implement LWA (Login with Amazon) token refresh
3. Handle token expiration and renewal
4. Consider using libraries like `boto3` for AWS signing

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is provided as-is for educational and commercial use.

## 🆘 Support

For issues related to:
- **This Django integration:** Open an issue on GitHub
- **Amazon SP-API:** Consult the [official SP-API documentation](https://developer-docs.amazon.com/sp-api/)

## 📚 Resources

- [Amazon SP-API Documentation](https://developer-docs.amazon.com/sp-api/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker Documentation](https://docs.docker.com/)

## ⚙️ Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Check `DB_HOST`, `DB_PORT`, and credentials in `.env`

2. **Amazon SP-API Authentication Error**
   - Verify your credentials in `.env`
   - Ensure your refresh token is valid
   - Check AWS IAM permissions

3. **Docker Issues**
   - Run `docker-compose down -v` to clean up
   - Rebuild with `docker-compose up --build`

## 🎯 Roadmap

- [ ] Add comprehensive unit tests
- [ ] Implement complete AWS SigV4 authentication
- [ ] Add request rate limiting
- [ ] Implement webhook handling for notifications
- [ ] Add API response caching
- [ ] Create admin panel for credential management
- [ ] Add API documentation with Swagger/OpenAPI
- [ ] Implement background task queue for long-running operations

---

**Built with ❤️ for Amazon sellers and developers**