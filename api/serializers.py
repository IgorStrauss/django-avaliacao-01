from rest_framework import generics, serializers
from rest_framework.response import Response

from management_cars_city.models import Car, Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'lastname',
            'email',
            'cpf',
            'cellphone',
            'owner_car',
            'full_name',
            'username',
        ]


class PersonPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'name',
            'lastname',
            'email',
            'cellphone'
        ]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'owner',
            'model',
            'color'
        ]

    def validate(self, data):
        owner = data.get('owner')
        model = data.get('model')
        color = data.get('color')
        if owner.car_set.count() >= 3:
            raise serializers.ValidationError('Já possui número máximo de veículos')
        if Car.objects.filter(owner=owner, model=model).exists():
            raise serializers.ValidationError('Este modelo não pode ser selecionado')
        if Car.objects.filter(owner=owner, color=color).exists():
            raise serializers.ValidationError('Esta cor não pode ser selecionada')
        return data


class PersonCarSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'lastname',
            'email',
            'cpf',
            'cellphone',
            'full_name',
            'cars',
        ]

    def get_cars(self, person):
        cars = Car.objects.filter(owner=person)
        serializer = CarSerializer(cars, many=True)
        return serializer.data
