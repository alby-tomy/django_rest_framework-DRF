from django.urls import path
from djangorestapi_app.views import indexView, personView

urlpatterns = [
    path('index/', view=indexView, name='index'),
    path('person/', view=personView, name='person')
]