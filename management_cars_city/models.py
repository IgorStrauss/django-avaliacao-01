from django.db import models
from django.forms import ValidationError


class Person(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False,
                            verbose_name="Nome")
    lastname = models.CharField(
        max_length=15, blank=False, null=False, verbose_name="Sobrenome"
    )
    email = models.EmailField(blank=False, null=False, verbose_name="E-mail")
    cpf = models.CharField(max_length=14, blank=False, null=False,
                           verbose_name="CPF")
    cellphone = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        verbose_name="Celular",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Cadastrado em:",
    )
    owner_car = models.BooleanField(default=False, blank=False, null=False)

    @property
    def format_name(self):
        return f"{self.name}".capitalize()

    @property
    def format_last_name(self):
        return f"{self.lastname}".capitalize()

    @property
    def full_name(self):
        return f"{self.name} {self.lastname}"

    @property
    def username(self):
        return f"{self.name + self.cpf[:3]}".upper()

    @property
    def format_celular(self):
        return f"({self.cellphone[:2]}) {self.cellphone[2]}{self.cellphone[3:7]}-{self.cellphone[7:]}"

    @property
    def format_cpf(self):
        return f"{self.cpf[:3]}-{self.cpf[3:6]}-{self.cpf[6:9]}.{self.cpf[9:11]}"

    @property
    def format_status_owner_car(self):
        return 'Sim' if self.owner_car else 'Não'

    def __repr__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(choices=(
                        ('Hatch', 'Hatch'),
                        ('Sedã', 'Sedã'),
                        ('Conversivel', 'Conversivel')
                        ))
    color = models.CharField(choices=(
                            ('Amarelo', 'Amarelo'),
                            ('Azul', 'Azul'),
                            ('Cinza', 'Cinza')
                            ))
    owner = models.ForeignKey(Person, on_delete=models.DO_NOTHING)

    def __repr__(self):
        return '<Car %r>' % self.owner_id

    class Meta:
        unique_together = ('owner', 'color', 'model')

    def clean(self):
        if self.owner.car_set.count() >= 3:
            raise ValidationError('Já possui número máximo de veículos')
