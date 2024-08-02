from django.urls import path, include
from djangorestapi_app.views import indexView, personView, ClassPerson, personViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'team_player_details', personViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
    path('index/', view=indexView, name='index'),
    path('person/', view=personView, name='person'),
    path('classperson/', ClassPerson.as_view(), name='class-person')
]