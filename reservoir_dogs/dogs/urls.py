from django.urls import path

from .controllers import BreedDetail, BreedList, DogDetail, DogList


urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('breeds/', BreedList.as_view({'get': 'list', 'post': 'create'}), name='breed-list'),
    path('breeds/<int:pk>/',
         BreedDetail.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='breed-detail'),
]
