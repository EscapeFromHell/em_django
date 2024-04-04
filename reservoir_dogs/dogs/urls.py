from django.urls import include, path
from rest_framework import routers

from .controllers import BreedDetail, BreedList, DogDetail, DogList


router = routers.DefaultRouter()
router.register('breeds', BreedList, basename='breed-list')
router.register('breeds', BreedDetail, basename='breed-detail')

urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('', include(router.urls))
]
