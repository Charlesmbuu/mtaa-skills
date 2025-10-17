# Mtaa Skills - Local Service Marketplace

![Mtaa Skills](https://img.shields.io/badge/Mtaa-Skills-brightgreen)
![Django](https://img.shields.io/badge/Django-4.2.7-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)

A modern web platform connecting service seekers with verified local service providers in Kenya.

## 🚀 Current Progress - MVP LAUNCHED!

**✅ PHASE 1 COMPLETED - Foundation Built**
- Django project setup with custom User model
- Service categories and provider management
- Job posting system
- Beautiful Bootstrap UI
- Admin interface
- Database migrations applied
- Sample data created

## 📋 Features Implemented

### Core Functionality
- **User Management**: Custom User model with customer/provider roles
- **Service Categories**: Plumbing, Electrical, Cleaning, Tutoring
- **Provider Profiles**: Service providers with categories and rates
- **Job Posting**: Customers can post service requests
- **Admin Panel**: Full Django admin for data management

### Technical Stack
- **Backend**: Django 4.2.7
- **Database**: SQLite (development)
- **Frontend**: Bootstrap 5, Django Templates
- **Authentication**: Django built-in auth with custom User model

## 🏗️ Project Structure
mtaa_skills/

| Directory/File | Purpose |
|---------------|---------|
| `backend/` | Django project configuration |
| `users/` | Custom user authentication & management |
| `services/` | Service categories & provider profiles |
| `bookings/` | Job posting & booking system |
| `templates/` | HTML templates for frontend |
| `manage.py` | Django management script |

---
```
mtaa_skills/
├── backend/ # Django project
│ ├── init.py
│ ├── settings.py # Project configuration
│ ├── urls.py # URL routing
│ └── wsgi.py
├── users/ # Custom user management
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Custom User model
│ └── views.py
├── services/ # Service categories & providers
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # ServiceCategory & ServiceProvider models
│ ├── urls.py
│ └── views.py
├── bookings/ # Job posting & booking system
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Job model
│ ├── urls.py
│ └── views.py
├── templates/ # HTML templates
│ └── home.html # Main landing page
├── .gitignore # Git ignore rules
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── manage.py # Django management script
```


## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Django 4.2.7

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/mtaa-skills.git
cd mtaa-skills

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django==4.2.7 pillow

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
Access the Application
Website: http://127.0.0.1:8000

Admin Panel: http://127.0.0.1:8000/admin
```

---

# 🎯 Next Features in Development

- User registration & authentication forms

- Service provider verification system

- Payment integration (M-Pesa & Stripe)

- Review and rating system

- Search and filtering functionality

- Mobile-responsive design improvements

---

# 👥 Team
Samburu - Project Lead & Full Stack Developer

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

# 🤝 Contributing
We welcome contributions! Please feel free to submit pull requests or open issues for suggestions.

Built with ❤️ for Kenyan communities using Django & Python

text

## **2. Git Ignore File**

Make sure you have this `.gitignore` file in your project root:

**.gitignore**
```
Django
*.pyc
pycache/
*.pyo
*.pyd
.Python
env/
```

Database
```
*.db
*.sqlite3
db.sqlite3
```

Environment variables
```
.env
.venv
```

Static files
```
/staticfiles/
/media/
```

IDE
```
.vscode/
.idea/
*.swp
*.swo
```

OS
```
.DS_Store
Thumbs.db
```

Logs
```
*.log
```
