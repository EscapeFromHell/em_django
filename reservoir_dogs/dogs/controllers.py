from typing import Any

from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from dogs.models import Dog, Breed
from dogs.serializers import DogSerializer, BreedSerializer


class DogDetail(APIView):
    """
    Class-based API view controller for detailed dog information.
    """
    def __get_object(self, pk: int) -> Dog:
        """
        Return the dog instance with the given primary key.
        """
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Return detailed information about a specific dog.
        """
        dog = self.__get_object(pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Update dog information.
        """
        dog = self.__get_object(pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Delete a dog.
        """
        dog = self.__get_object(pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):
    """
    Class-based API view controller for the list of dogs.
    """
    def get(self, request: Request, format: Any = None) -> Response:
        """
        Return a list of all dogs.
        """
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request: Request, format: Any = None) -> Response:
        """
        Create a new dog.
        """
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(viewsets.ViewSet):
    """
    Class-based API viewset controller for detailed breed information.
    """

    def __get_object(self, pk: int) -> Breed:
        """
        Get the breed instance by pk.
        """
        return get_object_or_404(Breed, pk=pk)

    def retrieve(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Return detailed information about a specific breed.
        """
        breed = self.__get_object(pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def update(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Update breed information.
        """
        breed = self.__get_object(pk=pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int, format: Any = None) -> Response:
        """
        Delete a breed.
        """
        breed = self.__get_object(pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(viewsets.ViewSet):
    """
    Class-based API viewset controller for the list of breeds.
    """
    def list(self, request: Request, format: Any = None) -> Response:
        """
        Return a list of all breeds.
        """
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def create(self, request: Request, format: Any = None) -> Response:
        """
        Create a new breed.
        """
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
