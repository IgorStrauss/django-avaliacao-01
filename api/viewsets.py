from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (CarSerializer, PersonCarSerializer,
                             PersonSerializer)
from management_cars_city.models import Car, Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.order_by('-id')
    serializer_class = PersonSerializer

    @action(detail=True, methods=['patch', 'get'], url_path='update')
    def partial_update_person(self, request, *args, **kwargs):
        allowed_fields = ['name', 'lastname', 'email', 'cellphone']
        data = {k: v for k, v in request.data.items() if k in allowed_fields}
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.order_by('-id')


class PersonCarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonCarSerializer

    def get_queryset(self):
        return Person.objects.all()
