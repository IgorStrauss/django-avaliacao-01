from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (CarSerializer, PersonCarSerializer,
                             PersonSerializer)
from management_cars_city.models import Car, Person


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.order_by('-id')


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.order_by('-id')


class PersonCarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonCarSerializer

    def get_queryset(self):
        return Person.objects.all()
