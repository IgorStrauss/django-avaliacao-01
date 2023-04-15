from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=15)
    email = forms.EmailField()
    cpf = forms.CharField(max_length=11)
    cellphone = forms.CharField(max_length=11)


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
    owner = forms.CharField()
