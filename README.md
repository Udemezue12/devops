🛒 E-commerce API with Django REST Framework

📦 An advanced E-commerce backend built with Django + Django REST Framework (DRF).
It provides product listings, cart & order management, customer accounts, promotions, reviews, and JWT authentication — ready for integration with React, Vue, Angular, or Mobile Apps.

📖 About

This project is a scalable E-commerce REST API designed for real-world use cases.
It allows:

👥 Customers to browse products, manage carts, and place orders.

🛍️ Admins to manage products, collections, promotions, and inventory.

💳 Support for order processing & payment statuses.

⭐ Customers can leave reviews for products.

Built with best practices in Django, DRF, and Celery for asynchronous tasks.

✨ Features
🔐 Authentication & Users

JWT-based authentication (djangorestframework-simplejwt)

Customer registration & profile management

Membership tiers (Bronze, Silver, Gold)

🛍️ Product & Inventory

Products with collections, promotions, and images

Inventory tracking with validation

Product reviews

🛒 Cart & Orders

Cart management (add/update/remove items)

Orders linked to customers

Payment status tracking (Pending, Complete, Failed)

Order permissions (cancel_order, send_order)

💬 Extras

DRF nested routers for structured APIs

Caching with Redis (django-redis)

Background tasks with Celery & Flower monitoring

Social login (social-auth-app-django)

Locust load testing support

🛠️ Tech Stack

Backend: Django 5, Django REST Framework

Authentication: DRF SimpleJWT, Djoser, Social Auth

Database: SQLite (default), MySQL/PostgreSQL supported

Caching/Queue: Redis + Celery + Flower

Testing: Pytest, Model Bakery

Load Testing: Locust

Deployment: Gunicorn, Whitenoise, Docker-ready

📂 Project Structure
ecommerce-api/
│── core/                # Core project settings
│── store/               # Main app: products, customers, orders
│── tag/                 # Tagging system
│── likes/               # Likes/favorites
│── locustfiles/         # Load testing scripts
│── simply/              # Extra app (extensions/custom logic)
│── manage.py
│── requirements.txt
│── Procfile
│── db.sqlite3
│── pytest.ini
│── general.log

⚙️ Installation

Clone the repo

git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api


Create & activate a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create a superuser

python manage.py createsuperuser


Start the server

python manage.py runserver

🐳 Running with Docker

Build the container:

docker build -t ecommerce-api .


Run with Docker Compose (if docker-compose.yml added):

docker-compose up --build

📌 API Endpoints (Sample)
Products
GET    /api/products/  
POST   /api/products/  
GET    /api/products/{id}/  

Cart
GET    /api/carts/{id}/  
POST   /api/carts/{id}/items/  
PATCH  /api/carts/{id}/items/{item_id}/  
DELETE /api/carts/{id}/items/{item_id}/  

Orders
GET    /api/orders/  
POST   /api/orders/  
PATCH  /api/orders/{id}/  

Reviews
POST   /api/products/{id}/reviews/  
GET    /api/products/{id}/reviews/  

🚀 Deployment

Configured with Procfile for Gunicorn.

Static files served via Whitenoise.

Supports Docker & Heroku/Render deployment.

✅ Future Enhancements

🛒 Payment gateway integration (Stripe, Paystack)

📦 Shipment tracking API

📊 Admin dashboards with analytics

📱 Mobile app integration