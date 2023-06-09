# Generated by Django 4.2 on 2023-04-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management_cars_city", "0005_alter_car_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="color",
            field=models.CharField(
                choices=[("Amarelo", "Amarelo"), ("Azul", "Azul"), ("Cinza", "Cinza")],
                max_length=12,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="model",
            field=models.CharField(
                choices=[
                    ("Hatch", "Hatch"),
                    ("Sedã", "Sedã"),
                    ("Conversivel", "Conversivel"),
                ],
                max_length=12,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="cellphone",
            field=models.CharField(max_length=15, unique=True, verbose_name="Celular"),
        ),
        migrations.AlterField(
            model_name="person",
            name="cpf",
            field=models.CharField(max_length=14, unique=True, verbose_name="CPF"),
        ),
        migrations.AlterField(
            model_name="person",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="E-mail"),
        ),
    ]
