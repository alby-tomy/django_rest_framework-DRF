from django.urls import path
from djangorestapi_app.views import indexView, personView, ClassPerson

urlpatterns = [
    path('index/', view=indexView, name='index'),
    path('person/', view=personView, name='person'),
    path('classperson/', ClassPerson.as_view(), name='class-person')
]