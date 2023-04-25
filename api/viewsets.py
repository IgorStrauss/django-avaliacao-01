from rest_framework import viewsets

from api import serializers
from management_cars_city.models import Car, Person


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = Person.objects.order_by('-id')


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarSerializer
    queryset = Car.objects.order_by('-id')
