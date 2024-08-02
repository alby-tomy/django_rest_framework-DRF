from django.urls import path
from djangorestapi_app.views import indexView

urlpatterns = [
    path('index/', view=indexView, name='index'),
]