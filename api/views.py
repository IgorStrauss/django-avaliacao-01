from rest_framework import generics
from rest_framework.decorators import action

from api.serializers import CarSerializer, PersonSerializer
from management_cars_city.models import Car, Person


class ListPerson(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=True, methods=['get'], url_name='listar_persons')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ListCar(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class RegisterCar(generics.CreateAPIView):
    serializer_class = CarSerializer


@action(detail=True, methods=['get'], url_name='ja possue veiculo')
class ListPersonWithStatusOwnerCar(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.order_by('-id').filter(owner_car=True)


@action(detail=True, methods=['get'], url_name='oportunidade_de_vendas')
class ListPersonWithoutStatusOwnerCar(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.order_by('-id').filter(owner_car=False)
