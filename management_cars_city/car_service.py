
from django.core.exceptions import ValidationError


class CarServiceAPI:
    @staticmethod
    def validate_car_limits(owner):
        if owner.car_set.count() >= 3:
            raise ValidationError('Já possui número máximo de veículos')

        if Car.objects.filter(owner=owner, model=self.model).exists():
            raise ValidationError('Este modelo não pode ser selecionado')

        if Car.objects.filter(owner=owner, color=self.color).exists():
            raise ValidationError(
                'Esta cor não pode ser selecionada para este veículo')