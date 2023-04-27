from rest_framework import serializers

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


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'owner',
            'model',
            'color'
        ]
