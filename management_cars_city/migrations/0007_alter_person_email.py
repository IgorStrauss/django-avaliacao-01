# Generated by Django 4.2 on 2023-04-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management_cars_city", "0006_alter_car_color_alter_car_model_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="E-mail"),
        ),
    ]