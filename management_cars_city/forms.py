from django import forms

from .models import Car, Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'lastname',
            'email',
            'cpf',
            'cellphone'
        ]


class UpdatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'lastname',
            'email',
            'cellphone'
        ]


class CarForm(forms.Form):
    model_choices = (
        (1, 'Hatch'),
        (2, 'Sedã'),
        (3, 'Conversível'),
    )
    color_choices = (
        (1, 'Amarelo'),
        (2, 'Azul'),
        (3, 'Cinza'),
    )

    model = forms.ChoiceField(choices=model_choices)
    color = forms.ChoiceField(choices=color_choices)
    owner = forms.ModelChoiceField(queryset=Person.objects.all(),
                                   label='Owner Name', empty_label=None,
                                   to_field_name='name')

    class Meta:
        model = Car
        fields = '__all__'
