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

## Models and Serializers
#### 'models.py'
Defines the `Person` model with fields: `name`, `email`, `age`, and `password`.

### 'serializers.py'
Defines the `PersonSerializer` with custom validation.

## Views
### 'views.py'
Defines the 'personView' function to handle different HTTP methods for CRUD operations.

## Create api directory and  Configure URL
### create 'api' directory in base directory
- add `urls.py`
- add `__init__.py`
- connect api.url with djangorestapi.url
  ```python
  from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/',include('api.urls')),
    ]
  ```
- Add the view to app/urls.py
  ```python
  from django.urls import path
  from .views import personView
  
  urlpatterns = [
      path('index/', view=indexView, name='index'),
      path('person/', view=personView, name='person'),
  ]
  ```


## Testing the API
You can test the API using tools like Postman or Curl

### Example Curl Commands:
- GET request to retrive all persons:
  ```bash
  curl -X GET http://127.0.0.1:8000/api/person/
  ```
- POST request to create a new person:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/person/ -d '{"name": "John", "email": "john@example.com", "age": 25, "password": "John@123"}' -H "Content-Type: application/json"
  ```
- PUT request to update a person:
  ```bash
  curl -X PUT http://127.0.0.1:8000/api/person/ -d '{"id": 1, "name": "John", "email": "john@example.com", "age": 26, "password": "John@123"}' -H "Content-Type: application/json"
  ```
- PATCH request to partially update a person:
  ```bash
  curl -X PATCH http://127.0.0.1:8000/api/person/ -d '{"id": 1, "age": 27}' -H "Content-Type: application/json"
  ```
- DELETE request to delete a person:
  ```bash
  curl -X DELETE http://127.0.0.1:8000/api/person/ -d '{"id": 1}' -H "Content-Type: application/json"
  ```
