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
