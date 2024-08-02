# C R U D operation using Django-Rest-Framework and Validators
This project demonstrates how to perform CRUD (Create, Read, Update, Delete) operations using Django REST Framework. It includes model validation using serializers and custom validators.

## Prerequisites
- Python 3.x
- Django
- Django REST Framework

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/alby-tomy/django_rest_framework-DRF-.git
cd djangorestapi_pr
```

### 2.Create Virtual Environment and Activate it
```bash
python -m venv venv
source venv/bin/activate
```

### 3.Install the Required Packages
```bash
pip install django djangorestframework
```
### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a Superuser (optional)
```bash
python manage.py createsuperuser
```
### 6. Run the Development Server
```bash
python manage.py runserver
```

