from django.shortcuts import render
from rest_framework import authentication, generics, permissions
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

from api.serializers import CarSerializer, PersonSerializer
from management_cars_city.models import Car, Person


class ListPerson(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ListCar(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
